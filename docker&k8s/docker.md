##Docker的三个基本概念
###### Image(镜像)
###### Container(容器)
###### Repository(仓库)

###### 镜像是 Docker 运行容器的前提，仓库是存放镜像的场所，可见镜像更是 Docker 的核心

###### 进入容器：docker container exec -it 容器id
###### 退出容器：exit
###### 停止/启动容器：docker stop/run id
###### 镜像删除：

###### K8s：容器的自动化复制和部署。随时扩展或收缩容器规模，冰提供负载均衡。方便的容器升级。提供容器弹性（失效替换）

#####docker和虚拟机最大的不同，docker共用宿主机的内核，虚拟机中每个虚拟机中有单独的内核虚拟出来

#####Docker的优缺点
- 优点：轻量级：因为docker不用虚拟化内核，直接共享宿主机的内核，所以节省了很多资源，在同样的资源下可以启动更多的软件，同时启动速度也更快
- 缺点：docker的优点也是它的缺点，正是因为所有的容器都共享一个内核，如果其中一个容器将内核给"搞坏了"，那所有的容器就都无法正常工作了


#####Docker的隔离之三项关键技术
- 1、NameSpace 每启动一个docker进程就会分配一个网络名称空间，进行网络的隔离
- 2、联合文件系统 能够给每一个容器提供单独的视图，达到文件目录的隔离，这样就不会访问到其他容器的文件
- 3、Cgroups 资源隔离，限定当前进程使用资源大小，达到资源的隔离

```
#docker images命令查看当前机器中的所有镜像

#docker rmi {镜像名}命令将指定镜像删除;注意要用冒号指定镜像的版本，如果不写将默认为latest

#docker ps可查看当前运行的所有容器（docker ps -s -a 可查看包括已经退出的和SIZE）

#docker run -d --name=myjenkins jenkins,将jenkins命名为myjenkins，并在后台运行容器

#停止容器运行的话可以使用docker stop myjenkins命令,想要删除容器的话可以使用docker rm -f myjenkins命令(-f作用为删除正在运行的容器,否则会报错)

#端口映射：使用命令docker run -d --name myjenkins -p 8080:8080 -p 50000:50000 jenkins启动Jenkins服务(宿主机端口:容器端口)，这段命令的意思是将宿主机以myjenkins命名在后台运行，并将宿主机的8080端口请求转发到容器的8080端口上；
```

(docker实战)[http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html]

docker build 创建镜像
docker run通过容器来运行镜像
