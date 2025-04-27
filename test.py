from huggingface_hub import InferenceClient

client = InferenceClient()
print(client.list_deployments())  # Should not error if token works
