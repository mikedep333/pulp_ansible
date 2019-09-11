LOGGING = {
    "loggers": {
        "pulp_ansible.app.tasks.collection.import_collection": {
            "level": "INFO",
            "handlers": ["collection_import"],
            "propagate": False,
        }
    },
    "handlers": {
        "collection_import": {
            "level": "DEBUG",
            "class": "pulp_ansible.app.logutils.CollectionImportHandler",
            "formatter": "simple",
        }
    },
    "dynaconf_merge": True,
}