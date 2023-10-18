{{/* Define default values for the application */}}
{{- define "survivor-predictor.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* Define default labels for the application */}}
{{- define "survivor-predictor.labels" -}}
helm.sh/chart: {{ include "survivor-predictor.name" . }}
{{- end -}}

{{/* Define default name for the application */}}
{{- define "survivor-predictor.name" -}}
{{- default "myapp" .Chart.Name -}}
{{- end -}}
