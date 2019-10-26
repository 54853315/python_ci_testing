# API Python接口覆盖率测试脚本

需要以docker镜像的方式运行，在业务项目们的`gitlab-ci.yml`里用`stage - test`关联，当backend进行CI部署后，我们可以让它自动的跑一遍python测试脚本。



### Docker编译
在项目根目录(包含Dockerfile的目录)执行

```shell
docker build -t cipython:v0.0.1 .
```

### Docker运行 

```shell
docker run -it cipython:v0.0.1
```

### 进入容器

```
docker run -it cipython:v0.0.1 /bin/bash
```

进去后可以看下python装在哪里，WORKDIR的 `/app` 下有没有程序代码。

### 容器里进行测试

```bash
nose2
```



# CI配置

[接口覆盖率集成gitlab-ci行动指南](https://blog.crazyphper.com/2019/10/26/python接口覆盖率集成gitlab-ci行动指南/)

