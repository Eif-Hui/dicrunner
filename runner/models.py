from django.db import models


# Create your models here.
class BaseTable(models.Model):
    class Meta:
        abstract = True
        db_table = 'BaseTable'

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)


class Project(BaseTable):
    class Meta:
        db_table = "project"

    name = models.CharField("项目名称", unique=True, max_length=100, null=False,help_text='项目名称')
    env_config = models.CharField("环境配置", max_length=100, null=False,help_text='环境配置')


class EnvVar(BaseTable):
    class Meta:
        db_table = "env_var"
        unique_together = (("project_id", "env_name", "name"),)

    name = models.CharField("变量名", max_length=50, null=False,help_text='变量名')
    value = models.CharField("变量值", max_length=100, null=False,help_text='变量值')
    desc = models.CharField("描述", max_length=200, default="",help_text='描述')
    project_id = models.IntegerField("项目id", null=False,help_text='项目id')
    env_name = models.CharField("环境名称", max_length=20, null=False,help_text='环境名称')


class Fixture(BaseTable):
    class Meta:
        db_table = "fixture"

    name = models.CharField("fixture名称", max_length=100, null=False,help_text='fixture名称')
    desc = models.CharField("fixture描述", max_length=500, default="",help_text='fixture描述')
    code = models.TextField("代码", max_length=30000, null=False,help_text='代码')
    creator_nickname = models.CharField("创建人昵称", null=False, max_length=64,help_text='创建人昵称')
    project_id = models.IntegerField("项目id", null=False,help_text='项目id')


class Case(BaseTable):
    class Meta:
        db_table = "case"

    desc = models.CharField("用例描述", max_length=500, null=False,help_text='用例描述')
    code = models.TextField("代码", max_length=30000, null=False,help_text='代码')
    creator_nickname = models.CharField("创建人昵称", null=False, max_length=64,help_text='创建人昵称')
    project_id = models.IntegerField("项目id", null=False,help_text='项目id')


class CaseResult(BaseTable):
    class Meta:
        db_table = "case_result"

    case_id = models.IntegerField("用例id", null=False,help_text='用例id')
    result = models.CharField("运行结果", max_length=50, null=False,help_text='运行结果')
    elapsed = models.CharField("耗时", max_length=50, null=False,help_text='耗时')
    output = models.TextField("输出日志", null=False, default="",help_text='输出日志')
    run_env = models.CharField("运行环境", max_length=20, null=False,help_text='运行环境')
    run_user_nickname = models.CharField("运行用户昵称", null=False, max_length=64,help_text='运行用户昵称')
    run_time = models.DateTimeField("运行时间", auto_now=True,help_text='运行时间')
