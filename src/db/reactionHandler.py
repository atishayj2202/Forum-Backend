from sqlalchemy import text


def addLike(Session, pid):
    session = Session()
    try:
        session.execute(statement=text("UPDATE articles SET likes = likes + 1 WHERE id = :el1;"), params={"el1": pid})
        session.commit()
        return {"Status": "Success"}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}


def addUnLike(Session, pid):
    session = Session()
    try:
        session.execute(statement=text("UPDATE articles SET unlikes = unlikes + 1 WHERE id = :el1;"),
                        params={"el1": pid})
        session.commit()
        return {"Status": "Success"}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}


def addComment(Session, pid, body, author_name, author_id):
    session = Session()
    try:
        session.execute(statement=text(
            "INSERT INTO article_comments (article_id, author_id, author_name, comment_text) VALUES (:el1, :el2, :el3, :el4);"),
            params={"el1": pid, "el2": author_id, "el3" : author_name, "el4":body})
        session.commit()
        return {"Status": "Success"}
    except:
        return {"Status": "Error", "Data": "Unexpected Error"}