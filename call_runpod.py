import base64
import json
import requests
import wave

url = "https://api.runpod.ai/v2/xxxxxxxxxx/runsync"
api_key = "GFD304XXXXXXXXXXGP2Y7GYE635"

text = "はーい、みなさーん、こちららんぽっどのAPI経由での音声です！"
file_path = "runpod_test_voice.wav"
model_id = 1


# APIから音声データを取得する関数
def fetch_audio_from_api(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "input": {
            "action": "/voice",
            "model_id": model_id,
            "text": text,
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()["output"]["voice"]
    else:
        raise Exception(f"API call failed with status code {response.status_code}")


# base64エンコードされた音声データをデコードしてファイルに保存する関数
def save_audio_file(base64_data, file_path):
    audio_data = base64.b64decode(base64_data)
    with open(file_path, "wb") as file:
        file.write(audio_data)


# wavファイルの情報をチェックする関数
def check_wav_file_info(file_path):
    with wave.open(file_path, "rb") as wav_file:
        print(f"Channels: {wav_file.getnchannels()}")
        print(f"Sample width: {wav_file.getsampwidth()}")
        print(f"Frame rate (sample rate): {wav_file.getframerate()}")
        print(f"Number of frames: {wav_file.getnframes()}")
        print(f"Params: {wav_file.getparams()}")


if __name__ == "__main__":
    try:
        # APIから音声データを取得
        base64_audio = fetch_audio_from_api(text)
        # ファイルに保存
        save_audio_file(base64_audio, file_path)
        print(f"Audio saved to {file_path}")
        # wavファイルの情報をチェック
        check_wav_file_info(file_path)
    except Exception as e:
        print(f"Error: {e}")
