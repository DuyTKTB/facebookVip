from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def fake_auth(cookie):
    # Giả lập xác thực cookie (bạn thay thế logic thật)
    return bool(cookie and cookie.strip())

@app.route('/')
def home():
    return "🚀 Server Facebook Tool đang chạy! Vui lòng gọi API đúng đường dẫn."

@app.route('/post', methods=['POST'])
def post():
    cookie = request.form.get('cookie')
    message = request.form.get('message')
    if not fake_auth(cookie):
        return jsonify(success=False, error="Cookie không hợp lệ")
    files_saved = []
    for key in ['image', 'video']:
        if key in request.files:
            f = request.files[key]
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            files_saved.append(filename)
    # Giả lập thành công đăng bài
    return jsonify(success=True, message="Đăng bài thành công", files=files_saved)

@app.route('/react', methods=['POST'])
def react():
    cookie = request.form.get('cookie')
    post_id = request.form.get('postID')
    reaction = request.form.get('reaction')
    if not fake_auth(cookie):
        return jsonify(success=False, error="Cookie không hợp lệ")
    if not post_id or not reaction:
        return jsonify(success=False, error="Thiếu postID hoặc reaction")
    # Giả lập thành công
    return jsonify(success=True, message=f"Đã thả cảm xúc {reaction} cho bài {post_id}")

@app.route('/comment', methods=['POST'])
def comment():
    cookie = request.form.get('cookie')
    post_id = request.form.get('postID')
    comment_text = request.form.get('comment')
    if not fake_auth(cookie):
        return jsonify(success=False, error="Cookie không hợp lệ")
    if not post_id or not comment_text:
        return jsonify(success=False, error="Thiếu postID hoặc comment")
    # Giả lập thành công
    return jsonify(success=True, message=f"Đã bình luận bài {post_id}")

@app.route('/share', methods=['POST'])
def share():
    cookie = request.form.get('cookie')
    post_id = request.form.get('postID')
    share_text = request.form.get('shareText')
    if not fake_auth(cookie):
        return jsonify(success=False, error="Cookie không hợp lệ")
    if not post_id:
        return jsonify(success=False, error="Thiếu postID")
    # Giả lập thành công
    return jsonify(success=True, message=f"Đã chia sẻ bài {post_id}")

if __name__ == '__main__':
    app.run(debug=True)
