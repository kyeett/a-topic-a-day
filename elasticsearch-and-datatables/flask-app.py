# An application that acts as a fake elasticsearch instance
# Returning a static JSON object 

from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)


# This route will return a list in JSON format
@app.route('/')
def index():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
    {
        "_index": "bookdb_index",
        "_type": "book",
        "_id": "4",
        "_score": 0.6259885,
        "_source": {
          "title": "Solr in Action",
          "authors": [
            "trey grainger",
            "timothy potter"
          ],
          "summary": "Comprehensive guide to implementing a scalable search engine using Apache Solr",
          "publish_date": "2014-04-05",
          "num_reviews": 23,
          "publisher": "manning"
        }
      },
      {
        "_index": "bookdb_index",
        "_type": "book",
        "_id": "3",
        "_score": 0.5975345,
        "_source": {
          "title": "Elasticsearch in Action",
          "authors": [
            "radu gheorge",
            "matthew lee hinman",
            "roy russo"
          ],
          "summary": "build scalable search applications using Elasticsearch without having to do complex low-level programming or understand advanced data science algorithms",
          "publish_date": "2015-12-03",
          "num_reviews": 18,
          "publisher": "manning"
        }
      },
      {
        "_index": "bookdb_index",
        "_type": "book",
        "_id": "2",
        "_score": 0.1975345,
        "_source": {
          "title": "Mistborn",
          "authors": [
            "brandon sanderson"
          ],
          "summary": "build scalable search applications using Elasticsearch without having to do complex low-level programming or understand advanced data science algorithms",
          "publish_date": "2017-12-03",
          "num_reviews": 1,
          "publisher": "manning"
        }
      }
    ]

    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(hits=list)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
