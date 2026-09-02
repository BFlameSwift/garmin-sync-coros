# Garmin ↔ COROS 双向同步

同步状态和 FIT 文件只保存在 Actions 运行时生成的 `db/`、`garmin-fit/`、`coros-fit/`
中。首次升级请删除旧的 `db/*.db` 后重新运行一次，让状态表按当前 schema 初始化。

重要：Garmin/COROS 密码只能配置为 GitHub Repository Secrets，不能写入代码、测试文件、
Issue 或日志。旧版本曾包含云端临时凭据，请立即轮换相关凭据，并把本次提交视为已暴露。
## 致谢
- 本脚本佳明模块代码来自@[yihong0618](https://github.com/yihong0618) 的 [running_page](https://github.com/yihong0618/running_page) 个人跑步主页项目,在此非常感谢@[yihong0618](https://github.com/yihong0618)大佬的无私奉献！！！

## DeepWiki源码解析
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/XiaoSiHwang/garmin-sync-coros)

## 注意
由于高驰平台只允许单设备登录，同步期间如果打开网页会影响到数据同步导致同步失败，同步期间切记不要打开网页。

## 参数配置
|       参数名       |                备注                |        案例        |
| :----------------: | :--------------------------------: | :----------------: |
|    GARMIN_EMAIL    |          佳明登录帐号邮箱          |                    |
|  GARMIN_PASSWORD   |            佳明登录密码            |                    |
| GARMIN_AUTH_DOMAIN | 佳明区域（国际区填:COM 国区填:CN） |    (COM or CN)     |
| GARMIN_NEWEST_NUM  |            最新记录条数            | (默认0，可写大于0) |
|    COROS_EMAIL     |           高驰 登录邮箱            |                    |
|   COROS_PASSWORD   |             高驰 密码              |                    |

必须配置以下 Repository Secrets：`GARMIN_AUTH_DOMAIN`（`CN` 或 `COM`）、`GARMIN_EMAIL`、
`GARMIN_PASSWORD`、`COROS_EMAIL`、`COROS_PASSWORD`，以及可选的 `GARMIN_NEWEST_NUM`。
两个 workflow 使用同一组账号，分别负责 Garmin→COROS 和 COROS→Garmin；并发锁会阻止两个
方向同时登录，避免 COROS 单设备登录互相踢下线。

## Github配置步骤
### 1.参数配置
打开**Setting**
![打开Setting](doc/3451692931372_.pic.jpg)
找到**Secrets and variables**点击**New repository secret**按钮
![Secrets and variables](/doc/3461692931472_.pic.jpg)
打开**New repository secret**后将上述的参数填入，下图以佳明帐号为例,**Name**填写参数名,**Secret**填写你的信息，重复以上步骤填入五个参数即可
![填入参数](doc/3471692931624_.pic.jpg)

### 2.配置WorkFlow权限
打开**Setting**找到**Actions**点击**General**按钮,按照下图勾选并save
![配置WorkFlow权限](doc/3481692931856_.pic.jpg)

### 3. wrokflow配置
打开**github/workflows/garmin-sync-coros.yml**文件,将**GITHUB_NAME**更改为你的Github用户名、**GITHUB_EMAIL**更改为你的Github登录邮箱，更改步骤如下:
![更改步骤](doc/3491692932110_.pic.jpg)
更改完成后点击右上角**Commit changes...**提交即可
![Commit](doc/3501692932345_.pic.jpg)

## 重新fork项目步骤
点击页面上**Sync Frok**然后点击**Dicard commit**即可
![fork sync](doc/image.png)
## 删除db步骤
按照图片顺序执行即可
![alt text](doc/image5.png)
![alt text](doc/image-1.png)
![alt text](doc/image-2.png)
![alt text](doc/image-3.png)
![alt text](doc/image-4.png)
删除完后等脚本自己执行即可
