┌──────────┐
│ GitHub   │
└────┬─────┘GitHub → CI/CD → Kubeflow → MLflow → LoRA → vLLM → FastAPI → Temporal → A2A → Agents → Redis → Qdrant → Vector Search → Ray → Kubernetes → Helm → ArgoCD → Langfuse → Prometheus → Grafana → DeepEval
     │
     ▼
┌──────────────┐
│ GitHub Actions│
└────┬─────────┘
     │
     ▼
┌──────────┐
│ Kubeflow │
└────┬─────┘
     │
     ▼
┌──────────┐
│ MLflow   │
└────┬─────┘
     │
     ▼
┌──────────┐
│ LoRA     │
└────┬─────┘
     │
     ▼
┌──────────┐
│ vLLM     │
└────┬─────┘
     │
     ▼
┌──────────┐
│ FastAPI  │
└────┬─────┘
     │
     ▼
┌──────────┐
│ Temporal │
└────┬─────┘
     │
     ▼
┌─────────────────────────────────────┐
│ A2A Agent Communication Layer       │
└────┬──────────┬──────────┬──────────┘
     │          │          │
     ▼          ▼          ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│Investigator│ │Planner │ │Executor│
└────┬────┘ └────┬────┘ └────┬────┘
     │           │           │
     └─────┬─────┴─────┬─────┘
           ▼           ▼
      ┌─────────┐  ┌─────────┐
      │ Redis   │  │ Qdrant  │
      └────┬────┘  └────┬────┘
           │            │
           └─────┬──────┘
                 ▼
      ┌─────────────────┐
      │ Vector Search   │
      │ + Reranking     │
      └───────┬─────────┘
              ▼
      ┌─────────────────┐
      │ Ray Cluster     │
      └───────┬─────────┘
              ▼
      ┌─────────────────┐
      │ Kubernetes      │
      └───────┬─────────┘
              ▼
      ┌─────────────────┐
      │ Helm + ArgoCD   │
      └───────┬─────────┘
              ▼
      ┌─────────────────┐
      │ Production      │
      └───────┬─────────┘
              ▼
      ┌─────────────────┐
      │ Langfuse        │
      │ Prometheus      │
      │ Grafana         │
      │ DeepEval        │
      └─────────────────┘
