# 基于 revChatGPT 和 flask 的简易 ChatGPT API

## usage

1. 在 config 配置你的ChatGPT access_token
   ```angular2html
   config={
       "proxy": "http://localhost:10809",
       "access_token": "<access_token>"
   }
   ```

2. 对 http://127.0.0.1/chat 发送带`msg参数`的的`post`包即可使用