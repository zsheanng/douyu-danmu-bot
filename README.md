# README.md
```markdown
# douyu-danmu-bot
斗鱼直播间自动弹幕发送脚本，基于Selenium调用本地Edge浏览器，弹幕随机间隔15~30秒。
> ⚠️ 重要提醒：使用第三方自动化脚本发送弹幕违反斗鱼用户协议，本项目仅用于Python编程学习，请勿长时间挂机使用，账号封禁风险自行承担。

## 一、前置准备
### 1. 环境依赖
1. 安装 Python 3.10+
2. 安装 Git（可选，用于代码版本管理）
3. 安装 selenium 库
pip install selenium
4. Edge浏览器（系统自带，无需额外下载）

### 2. 项目文件说明
项目目录 `danmuBot` 内必须包含2个文件：
- `main.py`：主运行脚本
- `danmu.json`：弹幕文案库（标准JSON数组格式）

### 3. danmu.json 标准示例
```json
[
    "666主播加油",
    "画面真不错",
    "学到了学到了",
    "太强了主播",
    "支持主播！"
]
```
⚠️ 规范要求：必须使用英文标点，文件编码为UTF-8，不能为空。

## 二、环境验证
1. 验证Python是否可用
```powershell
python --version
```
正常输出版本号即代表安装成功。

2. 验证selenium依赖
```powershell
pip show selenium
```
出现版本信息代表依赖安装完成。

3. 验证项目文件完整性
进入项目目录执行：
```powershell
cd E:\code\python\danmuBot
ls
```
列表中存在 `main.py`、`danmu.json` 即可。

## 三、运行使用教程
### 1. 启动脚本
PowerShell执行命令：
```powershell
python -u "E:\code\python\danmuBot\main.py"
```

### 2. 登录操作流程
1. 运行后自动弹出Edge浏览器，加载指定斗鱼直播间；
2. 登录账号；
3. 登录成功后会加载一个新页面，回到旧页面刷新一下；
4. 回到PowerShell窗口按下回车，程序自动遍历所有标签。

### 3. 自动发送逻辑
- 读取 `danmu.json` 内文案循环发送；
- 每条弹幕随机等待 **15 ~ 30秒** 再发送；
- 控制台实时打印即将发送的弹幕与剩余等待时长。

### 4. 终止程序
激活PowerShell窗口，按下快捷键：`Ctrl + C`
