# 项目开发文档

## 一、项目概述

本项目是一个基于 **Django + DRF + Celery + Redis** 后端，以及 **Vue3 + Vite + Pinia + TailwindCSS** 前端的全栈网站。  
主要功能包括用户注册/登录、主题切换、YouTube 频道数据快照展示，以及前端日志采集。项目已完成 Docker 化，支持一键启动开发与生产环境。

部署模式：
- **后端**：Django ASGI（Daphne），REST API，JWT 认证（SimpleJWT），Celery 任务调度（Beat + Worker），Redis 缓存。
- **前端**：Vue3 单页应用，Nginx 托管，HTTPS。
- **数据库**：PostgreSQL。
- **缓存/任务队列**：Redis。

## 二、目录结构

```
channel_website/
├── backend/                      # 后端源码
│   ├── backend/                  # 核心配置（settings、urls、asgi、celery）
│   ├── core/                      # 公共工具、异常处理、自定义命令
│   ├── profiles/                  # 用户与认证模块
│   ├── pages/                     # 页面内容模块（YouTube 数据）
│   ├── logs/                      # 前端日志采集模块
│   └── requirements.txt
├── frontend/                      # 前端源码
│   ├── src/
│   │   ├── api/                   # API 请求封装
│   │   ├── assets/css/            # 全局样式（Tailwind）
│   │   ├── components/            # Vue 组件
│   │   ├── router/                 # 路由定义与守卫
│   │   ├── stores/                 # Pinia 状态管理
│   │   ├── utils/                  # 工具函数（错误处理、日志、Cookies）
│   │   └── views/                  # 页面视图
│   ├── Dockerfile
│   └── nginx.conf
├── docker-compose.yml              # 基础 Compose
├── docker-compose.dev.yml          # 开发环境配置
├── docker-compose.pro.yml          # 生产环境配置
├── Makefile                        # 快捷命令（已修正 prod/pro 一致性）
└── README_DEV.md                   # 本文件
```

## 三、工作流

### 1. 开发环境
```bash
make dev       # 启动开发环境（后台+前台+数据库+缓存）
make devdown   # 停止并删除容器
```

- Django 热重载（`backend` 挂载到容器）
- Vue 热更新（`frontend` 挂载到容器）
- Redis / Postgres 数据持久化到 `./data`

### 2. 生产环境
```bash
make pro       # 启动生产环境（Nginx + 压缩打包后的前端）
make prodown   # 停止生产环境
```

- Nginx 提供 HTTPS（`nginx.conf` 配置 443）
- 容器内需提供 `cert.pem` 与 `key.pem`

### 3. 后端任务调度
- `core/management/commands/init_tasks.py`：用于创建/更新 Celery Beat 任务（如定时抓取 YouTube 数据）
- Celery Worker 与 Celery Beat 在 Compose 中独立运行
- Redis 用作任务队列与缓存存储

## 四、功能模块

### 1. 用户与认证（profiles）
- 注册（唯一邮箱校验，自动创建 Profile）
- 登录（返回 access/refresh token 及有效期）
- 刷新 Token
- 获取个人信息（用户名、邮箱、头像）
- 更新用户名（长度限制校验）
- 上传头像（文件大小/MIME 类型限制，Pillow 压缩）

### 2. YouTube 数据快照（pages）
- Celery Beat 定时任务拉取 YouTube API 数据 → 存入 Redis
- API `/api/v1/pages/youtube_channel_snapshot/` 返回：
  - 频道缩略图 URL
  - 订阅数、视频数、播放量
  - 自定义字段 `since`（固定起始日期 → 当前的天数差）

### 3. 前端日志采集（logs）
- 前端统一 Logger（debug/info/warn/error）
- 收集浏览器信息 + 错误信息 → 批量发送到 `/api/v1/log/collect/`
- 后端批量插入数据库（FELog 模型）

### 4. 主题切换（useThemeStore）
- 主题状态持久化到 `localStorage`
- 根据系统 `prefers-color-scheme` 自动选择
- 切换时修改 `document.documentElement[data-theme]`

## 五、开发注意事项

1. **YouTube 配置来源优化**：`core/utils/youtube.py` 需改为从 `django.conf.settings` 获取 URL/Headers（当前直接 import base settings）
2. **部署前**：准备好 `.env` 文件（SECRET_KEY、DB、Redis、JWT、YouTube API Key）及 HTTPS 证书

## 六、下一步计划

- [ ] 实现 Celery 抓取 YouTube 数据的实际任务（`tasks.py`）
- [ ] 完善前端 YouTube 数据展示页面
- [ ] 前端错误日志界面（后端可分页返回 FELog）
- [ ] CI/CD 流程（构建、测试、部署）
- [ ] 增加单元测试（后端 API / 前端组件）
