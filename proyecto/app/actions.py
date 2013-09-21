from django.http import HttpResponse
from django.core import serializers

def export_json(modeladmin, request, queryset):
	response = HttpResponse(content_type="application/json")
	serializers.serialize("json",queryset,stream=response)

	return response

export_json.short_description = "Export to json"