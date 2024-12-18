db.add_documents([Document(page_content="there are rabbits in the yard", metadata={"location": "yard", "topic": "animals"}),
Document(page_content="ducks are also found in the yard", metadata={"location": "yard", "topic": "animals"})], ids=[1,2])

db.delete(ids=[2]
