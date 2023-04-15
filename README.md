# Cipher

## 概念
- 加入多種隨機要素來加強安全性及破解難度
- 加密使用先換位再代換的方式，重複 3 遍
- 加密順序：
  1. Row Transposition Cipher
  2. Baconian Cipher
  3. Rail Fence Cipher
  4. Affine Cipher
  5. Grille Cipher
  6. Gronsfeld Cipher
- 每種加密方法都是以原方法為核心下去修改，除了 Gronsfeld Cipher 以外，均能夠處理數字及大小寫字母
- 每種方法有不同的 key 格式，所以會透過 `_key_transform` 進行轉換