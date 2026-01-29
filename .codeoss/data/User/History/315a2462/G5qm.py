from django.contrib import admin
# JSONを見やすく表示するための機能
from django.utils.html import format_html
import json
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    # 一覧画面に表示する列
    list_display = ('id_short', 'doc_type_label', 'company', 'status_badge', 'created_at')
    
    # 右側の絞り込みフィルター
    list_filter = ('doc_type', 'status', 'company')
    
    # 検索ボックス（会社名やIDで検索可能）
    search_fields = ('company__name', 'id')
    
    # 編集画面のフィールド構成
    readonly_fields = ('created_at', 'updated_at', 'preview_ai_data')
    fieldsets = (
        ('基本情報', {
            'fields': ('company', 'facility', 'doc_type', 'status')
        }),
        ('ファイル', {
            'fields': ('file',)
        }),
        ('AI解析結果', {
            'fields': ('ai_data', 'preview_ai_data'),
            'classes': ('collapse',), # 初期状態では閉じておく
        }),
        ('管理情報', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    # IDを短く表示する（見やすさのため）
    def id_short(self, obj):
        return str(obj.id)[:8] + "..."
    id_short.short_description = "ID"

    # 文書タイプを日本語で表示
    def doc_type_label(self, obj):
        return obj.get_doc_type_display()
    doc_type_label.short_description = "文書タイプ"

    # ステータスを色付きで表示する（UI向上）
    def status_badge(self, obj):
        colors = {
            'PENDING': 'gray',
            'PROCESSING': 'orange',
            'CONFIRMED': 'blue',
            'APPROVED': 'green',
        }
        color = colors.get(obj.status, 'black')
        return format_html(
            '<span style="color: white; background-color: {}; padding: 3px 8px; border-radius: 3px;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = "ステータス"

    # JSONデータを見やすく整形して表示
    def preview_ai_data(self, obj):
        if not obj.ai_data:
            return "-"
        # JSONをきれいに整形して表示
        formatted_json = json.dumps(obj.ai_data, indent=2, ensure_ascii=False)
        return format_html('<pre>{}</pre>', formatted_json)
    preview_ai_data.short_description = "データプレビュー"