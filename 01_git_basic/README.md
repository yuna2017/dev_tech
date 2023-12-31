# 01_GIT_BASIC

主讲：李大海 [Email](mailto:o0x80t@outlook.com)

## 前言1111111111111111111111111111111111111111

大家好！很高兴和大家分享我们的第一堂课。这节课中，我们将讨论一种代码管理和多人协作工具——Git。

本节课需要大家提前准备以下工具：

* 一台大屏设备
* 能访问 Github 的网络
* 一个已经加入了 YUNA2017 组织的 Github 账号

## 版本控制222222222222222222222222222222222

什么是版本控制？相信大家在大一课程的学习中，可能遇到下面的情况：

```
.
├── 114514.docx
├── lggg刚改的.docx
├── 三级项目报告（第一版改）.docx
├── 三级项目报告（第一版）.docx
├── 三级项目报告（第二版114514）.docx
├── 三级项目报告（第二版Fix）.docx
├── 三级项目报告（第二版）.docx
└── 新建 Word 文档.docx
```

你可能需要一一打开这些文件来确定到底是 `114514.docx` 是最新款还是 lggg 刚改的是最新的文档。如果你在 DDL 将要结束的时候面对这个场面就更火大了。

这时候，就该版本控制出场了。

版本控制系统通过存储每次文件修改过程中产生的修订记录来记录文件的修改。就像持久化的编辑器撤销和恢复键一样。

所以：版本控制系统是由文件的修订记录驱动的。

## Git

### 历史

Git 的历史与 Linux 分不开关系。脾气暴躁的Linux 内核开发者linus由于忍受不了之前的版本控制系统的缺陷，从而动手开发了这个工具。如果你去搜索一下 git 这个英文单词的意思的话，你就知道 Linus 有多暴躁了。

### 使用

> 历届开发部部长都为部员的环境配置而感到头疼。而这种问题在第七届得到了解决。因为我们在云端。

很高兴 Github 推出了 Codespace 这一开发环境。 Codespace 是运行在云端的完整 Linux 系统，只要通过浏览器就可以启动它，并通过一个和 VSCode 长得很像的编辑器来控制它，在上面编写代码。在本节课（很可能也在之后的课程）中，我们的实验环境就是 Codespace 的终端。它为我们提供了 Git 命令。

在我们了解 Git 之前，需要先体验一下 Github。 Github 的基本组织方式是仓库。每个仓库都是一个 git 存储库。Github为每个用户的每个存储库都提供 Codespace 环境。为了启动它，我们需要将仓库克隆到我们自己的账户下。

克隆完成之后，点击右上角的 Code，并在 Codespace 选项卡启动一个新的 codespace。随后就来到了我们熟悉的 VSCode 界面。

### Git 的修改单位——Commit

Git 通过修订记录来追踪文件的版本。那么，如何度量单个版本呢？ git把度量权交给我们。如果你认为这些修改足够产生一个版本的话，就可以创建一个 commit。 一个 commit 包含自从上次 commit 之后的所有对文件进行修改的信息。

例如，你现在可以修改本文件，随便加点文字或者删除文字。在 VSCode 左侧窗格的一个类似叉子的图标右下角会显示出一个数字。这就代表了你现在对多少数量的文件进行了修订。

Git 知道你有时候不想对文件夹下的某些文件做追踪（例如你的密码和密钥），也有可能你只想把你这次修改其中的部分文件进行提交（例如，你想提交新编写的两个文件中的一个文件）。所以，当你新建一个文件时，你需要手动告诉 git 是否需要对此文件追踪修订版本。你需要手动在左侧窗格中将文件加入到修改中。加入完成后，你就可以准备生成一次 commit 了。在 Message 中输入你这次 commit 的备注，然后点击 Commit。

### Git 的存储结构

Git 的基本单位是 commit。 commit之间如何连接在一起？答案是靠指针。当你在项目中增加一个 commit 时，这个 commit 将指向上一个 commit。项目中的所有 commit 就由此连接起来，并形成了一个类似链表的结构。你可以在这些链表之间进行前进和后退，就像你在进行撤销和重做。

### 链表的进化——branch

假设你回退到了一个之前的 commit，并在它的基础上做了修改。如果你提交了这些修改，现在就发生冲突了：有两个commit的都指向同一个父commit。怎么办？答案是 branch。给这两个commit起一个独特的名字，后续对这两个分支的修改将接到相应branch的修改中去。这种想法造就了 git 的另一种用途——协同开发。

## Git 的协同开发

假设你和lggg在开发 ATRI。你们需要增加一个充电桩查询功能和劳动教育抢课功能。你和lggg一人开发一个功能。如果没有版本管理工具，你们可能需要将项目拷贝，进行各自修改，然后手动将代码合并。这个过程将会很繁琐，并且你的 QQ 里将会充斥着各种源代码文件。

现在有了 Git。你和lggg在原有的 git 项目中各自分支出一个branch，在各自的分支中开发。当你们都开发完后，再将两个分支合并到主分支中。 Git 在合并过程中会自动检查文件的增删冲突，并提示你们修正。你的QQ不再有各种源代码，整个开发流程很清净。

### 谁来存储修订记录？

现在遇到了问题。原本的 git 项目如何能够方便地访问？最佳答案是将仓库的副本存储在一台服务器上，由服务器向各个用户提供修订记录的服务。因此就有了 Github。

Github的服务器上存储了我们上传到 Github 的每个项目的修订记录。当你想要编写新项目时，只需要向它查询并下载修订记录，即可开始编写。 在这种模型中，每个用户和服务器都保存有全部修订记录，当某用户丢失修订时，只需要向服务器或其他节点查询即可。这也就是 Git 为何被称为 **分布式版本控制系统** 的原因。

## Github：PR，Issue 和 Stars

### PR：合并代码的方式

如何将你的更改提交到服务器上？如果你是项目的所有者，只需要将本机的修订记录提交（Push）到服务器即可。如果你只是项目的贡献者，那就需要向项目所有者提交 Pull Request，等到项目所有者审查通过后才能合并代码。

### Issue 和 Stars

直接上手讲喽

## 作业

如果你之前曾经使用过 Github ，相信你一定听说过在华人程序员里非常流行的一个 Github 入门项目：[komeiji-satori/Dress](https://github.com/komeiji-satori/Dress)。这是一个由程序员发起的女装项目，大家可以自由地在其中上传自己的着装照片，当然，服装性别可以和生理性别不对应。

非常不幸的是，如果你现在点击这个链接，会发现 Github 小章鱼告诉你这个链接 404 了。在前段时间，女装项目由于涉及过多个人隐私信息，故被所有者删除。当然，由于在互联网上保存信息非常容易，如果你感兴趣的话，你还可以访问由其他 Github 用户备份保存的项目副本。

当然，欣赏项目中的各式各样的照片不在今天的作业范围之内。为了还原这样一个潮流项目，我们在本仓库中建立了一个分支 `dress` 。各位的任务就是**提交一份你的照片（可以不是服装照片）到仓库中。请不要提交包含个人隐私信息和/或令人感到不适的照片**。这也是本课程的签到方式。