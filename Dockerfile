#starts froma small linux image that already has python 3.12
FROM python:3.12-slim

# installs uv, its the same tool on windows
RUN pip install --no-cache-dir uv 

# work inside the /app folder in the container
WORKDIR /app

# copy the project file that list the packages
COPY pyproject.toml uv.lock README.md ./

# copies my code 
COPY src ./src

# install the exact looked packages, without the dev tools (jupyter/matplotlib)
RUN uv sync --locked --no-dev

# copy my data 
COPY data ./data

# what to run when the container starts
CMD ["uv", "run", "--no-dev", "genshin-build-checker"]