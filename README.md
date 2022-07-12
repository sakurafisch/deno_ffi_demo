# deno ffi demo

## 环境

经测试，可以在 Windows 11 和 Arch Linux 使用。由于缺乏苹果设备，在该平台上尚未测试。

## win

```cmd
python clean.py
rustc --crate-type cdylib add.rs
deno run --allow-ffi --unstable ffi.ts
```

## arch linux

```zsh
python clean.py
rustc --crate-type cdylib add.rs
deno run --allow-ffi --unstable ffi.ts
```
