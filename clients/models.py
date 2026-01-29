from django.db import models
import uuid

# 1. 会社（法人）モデル
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("法人名", max_length=100)
    code = models.CharField("法人コード", max_length=20, unique=True)
    address = models.CharField("住所", max_length=200, blank=True)
    created_at = models.DateTimeField("登録日", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "法人"
        verbose_name_plural = "法人一覧"

# 2. 施設（事業所）モデル
class Facility(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 会社と紐付ける（親が消えたら子も消える設定）
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="所属法人")
    name = models.CharField("施設名", max_length=100)
    code = models.CharField("施設コード", max_length=20, unique=True)
    is_active = models.BooleanField("契約中", default=True)
    
    def __str__(self):
        return f"{self.company.name} - {self.name}"

    class Meta:
        verbose_name = "施設"
        verbose_name_plural = "施設一覧"