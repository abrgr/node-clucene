{
    "targets": [
        {
            "target_name": "clucene",
            "include_dirs": [
                "src"
            ],
            "cflags!": [ "-fno-exceptions" ],
            "cflags_cc!": [ "-fno-exceptions" ],
            "sources": ["src/clucene_bindings.cpp"],
            "link_settings": {
                "libraries": [
                    "-lclucene-core"
                ]
            }
        }
    ]
}
