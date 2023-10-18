{{/* Define default values for the application */}}
{{- define "myapp-chart.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* Define default labels for the application */}}
{{- define "myapp-chart.labels" -}}
helm.sh/chart: {{ include "myapp-chart.name" . }}
{{- end -}}

{{/* Define default name for the application */}}
{{- define "myapp-chart.name" -}}
{{- default "myapp" .Chart.Name -}}
{{- end -}}
