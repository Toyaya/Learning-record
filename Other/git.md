#####一. git pull不覆盖修改的代码：
'''
1.git stash save "这里是注释"
2.git pull
3.git stash pop
4.git stash list 
5.git stash show
'''

#####二.若想取消本地的修改：to discard changes in working directory
'''
git checkout -- <file>
'''
#####三.取消commit而不影响代码：
’‘’
git reset --soft HEAD^
‘’‘

#####四.创建新的分支，并提交代码
’‘’
1.git checkout develop
2. git pull origin develop
3. git checkout -b user/zhangsan
4. git add
5. git commit -m "this is comment"
6. git push origin user/zhangsan:"this is cloud branch name"
‘’‘