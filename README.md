# file-manager-challs

我在2026上半年出的pwn/misc系列CTF題目。

## 題目敘述

### File Manager 1

分類：Pwn / Misc

難度：Easy

```
Welcome to the file manager!
You can read files, calculate their hash, and create new files.

Flag Format: ZLCSC{*}
```

### File Manager 2

分類：Pwn / Misc

難度：Hard

```
I've fixed the vulnerability in the previous version (I won't be hacked again haha), deleted some unnecessary code, and added some new features.
Also, I introduce a new "Backup" feature!

Flag Format: ZLCSC{*}
```

### File Manager 3

分類：Pwn / Misc

難度：Hard

```
I can't believe it... my file manager got pwned TWICE already.
Anyway, I've fixed everything this time.
By the way, the backup restore feature is finally here!

Flag Format: ZLCSC{*}
```

## 如何開啟題目

cd 進題目個別的資料夾，然後

```bash
docker-compose up --build
```

三題分別會開在port 10001, 10002, 10003
解完欲關掉題目時再

```bash
docker-compose down
```

> 註：Instancer 是 ChatGPT 幫我弄的，我還不會弄。
> 註：出題與 exploit 撰寫過程用到有 ChatGPT, Gemini, Copilot AI 輔助。
