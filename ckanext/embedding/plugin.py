import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from sentence_transformers import SentenceTransformer
import json
import logging

log = logging.getLogger(__name__)

# import ckanext.embedding.cli as cli
# import ckanext.embedding.helpers as helpers
# import ckanext.embedding.views as views
# from ckanext.embedding.logic import (
#     action, auth, validators
# )


class EmbeddingPlugin(plugins.SingletonPlugin):
    # 임베딩 모델 로드
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # embedding_fields = [
    #     "title",
    #     "tags",
    #     "notes",
    # ]
    EMBEDDING_FIELD_NAME = "vector"

    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "embedding")

    # def configure(self, config):
    #     """CKAN 설정 파일로부터 설정을 읽어옵니다."""
    #     self.embedding_model_name = config.get('ckanext.vector_embedding.model', 'all-mpnet-base-v2')
    #     self.embedding_fields = [
    #         field.strip()
    #         for field in config.get('ckanext.vector_embedding.fields', 'title,notes').split(',')
    #         if field.strip()
    #     ]
    #     self.embedding_field_name = config.get('ckanext.vector_embedding.output_field', 'vector_embedding')
    #     self.model = SentenceTransformer(self.embedding_model_name)

    def before_dataset_index(self, pkg_dict):
        """데이터셋이 Solr에 인덱싱되기 전에 호출되는 훅입니다."""
        text_to_embed = ""
        text_to_embed = f"{pkg_dict.get('title', '')} {' '.join([tag for tag in pkg_dict.get('tags', [])])} {pkg_dict.get('notes', '')} {pkg_dict.get('pricing', '')} {pkg_dict.get('maintainer', '')}"
        # for field in self.embedding_fields:
        #     if field in pkg_dict:
        #         text_to_embed += pkg_dict[field] + " "

        if text_to_embed.strip():
            try:
                embeddings = self.model.encode(text_to_embed).tolist()
                # 임베딩 결과를 데이터셋 딕셔너리에 추가
                pkg_dict[self.EMBEDDING_FIELD_NAME] = embeddings
            except Exception as e:
                log.error(
                    f"Error generating embeddings for dataset {pkg_dict.get('id')}: {e}"
                )

        return pkg_dict

    def create_embedding(self, text):
        """주어진 텍스트에 대한 임베딩 벡터를 생성합니다."""
        if text:
            return self.model.encode(text).tolist()
        return None

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers
