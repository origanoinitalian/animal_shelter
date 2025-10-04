import kagglehub

# Download latest version
path = kagglehub.dataset_download("aaronschlegel/austin-animal-center-shelter-outcomes-and")

print("Path to dataset files:", path)