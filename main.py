
from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import top_articles
from content_filtering import get_recommendation




@app.route("/get_popular_articles", methods=["GET"])
def get_popular_articles():
    return jsonify(top_articles)



@app.route("/get_recommended_articles", methods=["GET"])
def get_recommended_articles():
    # Get the article_id from the request
    article_id = request.args.get("article_id")

    recommended_articles = get_recommendation(article_id)

    return jsonify(recommended_articles)

