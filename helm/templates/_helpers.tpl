{{/* Define default values for the application */}}
{{- define "ml-app.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* Define default labels for the application */}}
{{- define "ml-app.labels" -}}
helm.sh/chart: {{ include "ml-app.name" . }}
{{- end -}}

{{/* Define default name for the application */}}
{{- define "ml-app.name" -}}
{{- default "myapp" .Chart.Name -}}
{{- end -}}
