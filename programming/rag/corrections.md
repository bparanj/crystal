loader = WebBaseLoader(
    web_paths=["https://kbourne.github.io/chapter1.html"],  # Note: Using list instead of tuple
    bs_kwargs={
        'parse_only': bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    }
)

docs = loader.load()

