from flask import Flask
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy()
db.init_app(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of video")
video_put_args.add_argument("views", type=int, help="Views of video")

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}


def get_video(video_id):
    video = VideoModel.query.get(video_id)
    if not video:
        abort(404, message="Video does not exist")
    return video


def check_video_exists(video_id):
    if VideoModel.query.get(video_id):
        abort(404, message="Video already exists")


class Video(Resource):

    def get(self):
        video = VideoModel.query.filter_by()
        return video

    @marshal_with(resource_fields)
    def post(self):
        import pdb; pdb.set_trace()
        args = video_put_args.parse_args()
        video = VideoModel(name=args['name'],
                           views=args['views'],
                           likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return "", 201


class Videos(Resource):
    def get(self, video_id):
        video = get_video(video_id)
        return video

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        check_video_exists(video_id)
        video = VideoModel(id=video_id, name=args['name'],
                           views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def delete(self, video_id):
        video = get_video(video_id)
        db.session.delete(video)
        db.session.commit()
        return "", 204

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_put_args.parse_args()
        update_params = {}
        for arg in args:
            if args[arg]:
                update_params[arg] = args[arg]
        VideoModel.query.filter_by(id=video_id).update(values=update_params)
        db.session.commit()
        return "", 201


api.add_resource(Video, "/videos/")
api.add_resource(Videos, "/videos/<video_id>")


if __name__ == "__main__":
    app.run(debug=True)
