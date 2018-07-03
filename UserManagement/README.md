# 用户管理系统
这是负责用户认证的App

## Django Admin 的使用
Django admin 的用户对应本系统中的职务，职务与权限直接对应，本系统中的User才是真正的用户，一人一个用户。

## 用户认证
所有用户认证代码在 `Authentication.py` 中。认证完成后，用户的ID和密码将会保存在session中。  
此处应当使用sso认证。


## 部门树管理
- 部门列表（含有上级部门，上级部门可为空）
- 部门职务（将职务与部门绑定）
- 任职表（用户与职务绑定，当人员更改后，只需要更改用户绑定的职务就可以直接更改权限）

职务权限（职务与权限绑定，以防人员流动，修改次数多）

## session
|名称|解释|
|---|---|
|user_id|用户id|
|user_pwd|用户密码|
|admin_set|对应的职务集合|
|perm_set|对应的权限集合|

## 权限
### 用户（教师/本科生/研究生）
#### 查看
- 查看所有用户：view_all_users
    - 查看所有教师：view_all_teachers
    - 查看所有本科生：view_all_us
    - 查看所有研究生：view_all_gs
- 查看自己年级学生：view_grade_users, view_grade_us, view_grade_gs（年级辅导员也适用）
- 查看自己班级学生：view_class_users, view_class_us, view_class_gs（班导师也适用）
- 查看自己导师研究生：view_teacer_gs（导师也适用）
- 查看自己创建的用户：view_my_users
    - 查看自己创建的教师用户：view_my_teachers
    - 查看自己创建的本科生：view_my_us
    - 查看自己创建的研究生：view_my_gs
#### 增加
- 增加用户：create_user
    - 增加教师用户：create_teacher
    - 增加本科生：create_us
    - 增加研究生：create_gs
#### 修改
- 修改所有用户：update_all_users
    - 修改所有教师：update_all_teachers
    - 修改所有本科生：update_all_us
    - 修改所有研究生：update_all_gs
- 修改自己年级学生：update_grade_users, update_grade_us, update_grade_gs（年级辅导员也适用）
- 修改自己班级学生：update_class_users, update_class_us, update_class_gs（班导师也适用）
- 修改自己导师研究生：update_teacer_gs（导师也适用）
- 修改自己创建的用户：update_my_users
    - 修改自己创建的教师用户：update_my_teachers
    - 修改自己创建的本科生：update_my_us
    - 修改自己创建的研究生：update_my_gs
#### 删除
- 删除所有用户：delete_all_users
    - 删除所有教师：delete_all_teachers
    - 删除所有本科生：delete_all_us
    - 删除所有研究生：delete_all_gs
- 删除自己年级学生：delete_grade_users, delete_grade_us, delete_grade_gs（年级辅导员也适用）
- 删除自己班级学生：delete_class_users, delete_class_us, delete_class_gs（班导师也适用）
- 删除自己导师研究生：delete_teacer_gs（导师也适用）
- 删除自己创建的用户：delete_my_users
    - 删除自己创建的教师用户：delete_my_teachers
    - 删除自己创建的本科生：delete_my_us
    - 删除自己创建的研究生：delete_my_gs

## Todo List
- 大部分Manager方法也应该是模型类方法