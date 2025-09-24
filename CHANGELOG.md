# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Added git cliff git eg for changelog
- Add ROADMAP of Kubeflow SDK by @kramaranya
- Add unit test for trainer sdk by @briangallagher
- Add e2e notebook tests by @briangallagher
- Add support for UV & Ruff by @szaher
- Add CONTRIBUTING.md by @abhijeet-dhumal
- Add pre-commit and flake8 configs by @eoinfennessy
- Add Stale GitHub action by @kramaranya
- Add missing import type Initializer. (kubeflow/trainer#2541) by @Electronic-Waste
- Add e2e test for train API (kubeflow/trainer#2199) by @helenxie-bit
- [SDK] test: add unit test for get_job_logs method of the training_client (kubeflow/trainer#2275) by @seanlaii
- [SDK] test: add unit test for list_jobs method of the training_client (kubeflow/trainer#2267) by @seanlaii
- Add JAX controller (kubeflow/trainer#2194) by @sandipanpanda
- [SDK] test: add unit test for get_job method of the training_client (kubeflow/trainer#2205) by @Bobbins228
- [SDK] test: add unit tests for delete_job() method (kubeflow/trainer#2232) by @Bobbins228
- Add JAX API (kubeflow/trainer#2163) by @sandipanpanda
- Support Python 3.11 and Drop Python 3.7 (kubeflow/trainer#2105) by @tenzen-y
- Adding fine tune example with s3 as the dataset store (kubeflow/trainer#2006) by @deepanker13
- Add Fine-Tune BERT LLM Example (kubeflow/trainer#2021) by @andreyvelich
- Adding Training image needed for train api (kubeflow/trainer#1963) by @deepanker13
- Add test to create PyTorchJob from func (kubeflow/trainer#1979) by @andreyvelich
- Add check pods are not scheduled when testing gang-scheduler integrations in e2e (kubeflow/trainer#1835) by @tenzen-y
- Add E2E test for gang-scheduling (kubeflow/trainer#1736) by @tenzen-y
- Add clientset for MPIJob, PytorchJob, MXJob, and XGBoostJob (kubeflow/trainer#1610) by @tenzen-y
- Adding MPI python sdk (kubeflow/trainer#1608) by @johnugeorge
- Adding XGboost Python sdk  (kubeflow/trainer#1607) by @johnugeorge
- Add Python SDK for Kubeflow Training Operator (kubeflow/trainer#1420) by @alembiewski
- Add watch function for TFJob python Client API (kubeflow/trainer#1122) by @jinchihe
- Add API to wait for TFJob done (kubeflow/trainer#1116) by @jinchihe
- Add GitHub issue and PR templates by @eoinfennessy

### Changed
- Github default format
- Kubeflow SDK Official Release 0.1.0 by @kramaranya
- Kubeflow SDK Official Release 0.1.0rc1 by @kramaranya
- Ignore PRs titles with area/release labels in CI by @kramaranya
- Add automated release CI job by @kramaranya
- Add proper ruff configuration by @szaher
- Implement TrainerClient Backends & Local Process by @szaher
- Update CONTRIBUTING.md to use uv by @szaher
- KEP-2 Local Execution Mode Proposal by @szaher
- Add welcome new contributors CI by @kramaranya
- Add support for param unpacking in the training function call by @briangallagher
- Support multiple pip index URLs in CustomTrainer by @wassimbensalem
- Refactor get_job_logs() API with Iterator by @andreyvelich
- Use explicit exception chaining by @andreyvelich
- Nominate @kramaranya and @szaher as Kubeflow SDK reviewers by @andreyvelich
- Enable parallel builds for coveralls by @kramaranya
- Remove tool.hatch.build.targets from pyproject by @kramaranya
- Move dev extras to dependency-groups by @kramaranya
- Update README.md by @kramaranya
- Implement Kubernetes Backend by @szaher
- Move pyproject.toml to root by @kramaranya
- Add `get_runtime_packages()` API by @andreyvelich
- Align Kubernetes versions from Trainer for e2e tests by @astefanutti
- Add dev tests with master dependencies by @kramaranya
- Support Framework Labels in Runtimes by @andreyvelich
- Add environment variables argument to CustomTrainer by @astefanutti
- Add `wait_for_job_status()` API by @andreyvelich
- Add Coveralls Badge to the README by @andreyvelich
- Remove accelerator label from the runtimes by @andreyvelich
- Add GitHub action to verify PR titles by @andreyvelich
- Update pyproject.toml project links by @szaher
- Step down from sdk ownership role by @tenzen-y
- Reflect owners updates from KF Trainer by @tenzen-y
- Consume Trainer models from external package kubeflow_trainer_api by @kramaranya
- Move commits from `kubeflow/trainer` by @szaher
- Support mutating dataset preprocessing config in SDK (kubeflow/trainer#2638) by @Electronic-Waste
- Revert "fix(sdk): Fix type annotation for `train` method's `trainer` parameter" (kubeflow/trainer#2651) by @Electronic-Waste
- Move generated Python models into kubeflow_trainer_api package (kubeflow/trainer#2632) by @kramaranya
- Complement torch plugin to support torchtune config mutation (kubeflow/trainer#2587) by @Electronic-Waste
- Get namespace from the provided context (kubeflow/trainer#2593) by @andreyvelich
- Support MLX Distributed Runtime with OpenMPI (kubeflow/trainer#2565) by @andreyvelich
- Add `TorchTuneConfig` to `train()` API (kubeflow/trainer#2522) by @Electronic-Waste
- Support DeepSpeed Runtime with OpenMPI (kubeflow/trainer#2559) by @andreyvelich
- Support MPI-based TrainJobs  (kubeflow/trainer#2545) by @andreyvelich
- Refactor the Initializer APIs of TrainJob (kubeflow/trainer#2523) by @andreyvelich
- Fix kubeflow/trainer#2407: Cap nproc_per_node based on CPU resources for PyTorch TrainJob by @Diasker
- Refactor current `train()` API (kubeflow/trainer#2513) by @Electronic-Waste
- Migrate to OpenAPI V3 (kubeflow/trainer#2490) by @andreyvelich
- Integrate DependsOn API (kubeflow/trainer#2484) by @andreyvelich
- Implement MPI numProcPerNode defaulter (kubeflow/trainer#2483) by @tenzen-y
- Generate external Kubernetes and JobSet models (kubeflow/trainer#2466) by @andreyvelich
- Add E2E tests for Kubeflow Trainer (kubeflow/trainer#2470) by @andreyvelich
- Bump JobSet to v0.8.0 (kubeflow/trainer#2463) by @andreyvelich
- Upgrade jobset SDK version to v0.7.3 (kubeflow/trainer#2445) by @Electronic-Waste
- Add validation to Torch `numProcPerNode` field (kubeflow/trainer#2409) by @astefanutti
- Implement MPI Plugin for Kubeflow Trainer (kubeflow/trainer#2394) by @andreyvelich
- Update the naming conventions for Kubeflow Trainer  (kubeflow/trainer#2415) by @andreyvelich
- Testing CI in JAX example (kubeflow/trainer#2385) by @saileshd1402
- Fix versions in HuggingFace dataset initializer (kubeflow/trainer#2369) by @andreyvelich
- [SDK] Adding env vars (kubeflow/trainer#2285) by @tarekabouzeid
- [SDK] Initial implementation of the Kubeflow Training V2 Python SDK (kubeflow/trainer#2324) by @andreyvelich
- Upgrade Kubernetes to v1.31.3 (kubeflow/trainer#2330) by @astefanutti
- Pin accelerate package version in trainer (kubeflow/trainer#2340) by @gavrissh
- Upgrade Kubernetes to v1.30.7 (kubeflow/trainer#2332) by @astefanutti
- [SDK] Use torchrun to create PyTorchJob from function (kubeflow/trainer#2276) by @andreyvelich
- [SDK] Training Client Conditions related unit tests (kubeflow/trainer#2253) by @Bobbins228
- [SDK] Minor fix in wait_for_job_conditions with job_kind python training API (kubeflow/trainer#2265) by @saileshd1402
- [SDK] move env var to constants.py (kubeflow/trainer#2268) by @varshaprasad96
- Update JAX image to use image published by Kubeflow  (kubeflow/trainer#2264) by @sandipanpanda
- [SDK] Allow customising base trainer and storage images in Train API (kubeflow/trainer#2261) by @varshaprasad96
- [Feature] Support managed by external controller (kubeflow/trainer#2203) by @mszadkow
- Bump Training Python SDK to 1.8.1 version (kubeflow/trainer#2257) by @andreyvelich
- [SDK] Read namespace from the current context (kubeflow/trainer#2255) by @andreyvelich
- [SDK] Fix typo of "get_pvc_spec" (kubeflow/trainer#2250) by @helenxie-bit
- [SDK] Add UTs for `wait_for_job_conditions` (kubeflow/trainer#2196) by @Electronic-Waste
- [SDK] Fix trainer error: Update the version of base image and add "num_labels" for downloading pretrained models (kubeflow/trainer#2230) by @helenxie-bit
- Change isort profile to black for full compatibility (kubeflow/trainer#2234) by @Ygnas
- [SDK] Unit tests for TrainingClient APIs - get_job_pod_names and update_job (kubeflow/trainer#2192) by @YosiElias
- Enhance pre-commit hooks with flake8 linting (kubeflow/trainer#2195) by @Ygnas
- Update trainer to ensure type consistency for `train_args` and `lora_config` (kubeflow/trainer#2181) by @helenxie-bit
- Update the name of PVC in `train` API (kubeflow/trainer#2187) by @helenxie-bit
- Implement pre-commit hooks (kubeflow/trainer#2184) by @droctothorpe
- Update `huggingface_hub` Version in the storage initializer to fix ImportError (kubeflow/trainer#2180) by @helenxie-bit
- [SDK] Add more unit tests for TrainingClient APIs - get_job_pods (kubeflow/trainer#2175) by @YosiElias
- Bump Training Python SDK to 1.8.0 version (kubeflow/trainer#2172) by @andreyvelich
- [SDK] Fix Failed condition in wait Job API (kubeflow/trainer#2160) by @andreyvelich
- [SDK] Sync Transformers version for train API (kubeflow/trainer#2146) by @andreyvelich
- [SDK] Explain Python version support cycle (kubeflow/trainer#2144) by @andreyvelich
- Update Slack Invitation (kubeflow/trainer#2142) by @andreyvelich
- [SDK] Fix Incorrect Events in get_job_logs API (kubeflow/trainer#2122) by @andreyvelich
- Changed package name to flake8 to fix pytests pip install (kubeflow/trainer#2109) by @ChristopheBrown
- Replace outdated images with latest ones (kubeflow/trainer#2083) by @tenzen-y
- [SDK] Add docstring for Train API (kubeflow/trainer#2075) by @andreyvelich
- Upgrade the minimum required Kubernetes version to v1.27.2 (kubeflow/trainer#2066) by @tenzen-y
- Bump transformers from 4.37.2 to 4.38.0 in /sdk/python/kubeflow/storage_initializer (kubeflow/trainer#2056) by @dependabot[bot]
- Bump transformers from 4.37.2 to 4.38.0 in /sdk/python/kubeflow/trainer (kubeflow/trainer#2055) by @dependabot[bot]
- Bump black from 21.12b0 to 24.3.0 in /sdk/python (kubeflow/trainer#2033) by @dependabot[bot]
- Modify LLM Trainer to support BERT and Tiny LLaMA (kubeflow/trainer#2031) by @andreyvelich
- Fix URL in python SDK setup.py (kubeflow/trainer#2011) by @garymm
- [SDK] Add resources per worker for Create Job API (kubeflow/trainer#1990) by @andreyvelich
- [SDK] Fix Worker and Master templates for PyTorchJob (kubeflow/trainer#1988) by @andreyvelich
- Publish trainer hugging face image (kubeflow/trainer#1985) by @deepanker13
- [SDK] Get Kubernetes Events for Job (kubeflow/trainer#1975) by @andreyvelich
- [SDK] Train API (kubeflow/trainer#1962) by @deepanker13
- [SDK] Add information about TrainingClient logging (kubeflow/trainer#1973) by @andreyvelich
- Train api dataset download changes (kubeflow/trainer#1959) by @deepanker13
- Train api init container creation (kubeflow/trainer#1958) by @deepanker13
- Utils changes needed to add train api (kubeflow/trainer#1954) by @deepanker13
- Training operator SDK unit test (kubeflow/trainer#1938) by @deepanker13
- Avoid modifying log level globally (kubeflow/trainer#1944) by @droctothorpe
- Merge v1.7 branch changes to Main (kubeflow/trainer#1940) by @johnugeorge
- Use a community hosted image in MXJob E2E (kubeflow/trainer#1928) by @tenzen-y
- Replace XGBoost image for E2E with community hosted (kubeflow/trainer#1922) by @tenzen-y
- [SDK] Consolidate Naming for CRUD APIs (kubeflow/trainer#1907) by @andreyvelich
- Implement suspend semantics (kubeflow/trainer#1859) by @tenzen-y
- Make Condition and ReplicaStatus optional (kubeflow/trainer#1862) by @tenzen-y
- Set correct ENV for PytorchJob to support torchrun (kubeflow/trainer#1840) by @kuizhiqing
- Merge kubeflow/common to training-operator (kubeflow/trainer#1813) by @johnugeorge
- Make scheduler-plugins the default gang scheduler. (kubeflow/trainer#1747) by @Syulin7
- Improve E2E tests for the gang-scheduling (kubeflow/trainer#1801) by @tenzen-y
- Make timeout configurable from e2e tests (kubeflow/trainer#1787) by @nagar-ajay
- Containerize e2e tests for training operator conformance (kubeflow/trainer#1780) by @nagar-ajay
- Disable istio-sidecar injection (kubeflow/trainer#1778) by @nagar-ajay
- E2e test in k8s cluster and Namespace option (kubeflow/trainer#1774) by @nagar-ajay
- Fix XGBoost flaky e2e tests (kubeflow/trainer#1775) by @nagar-ajay
- [Bugfix][SDK] pod has no metadata attr anymore in the get_job_logs() … (kubeflow/trainer#1760) by @yaobaiwei
- [SDK] Use Training Client without Kube Config (kubeflow/trainer#1740) by @andreyvelich
- Adopting coschduling plugin (kubeflow/trainer#1724) by @tenzen-y
- [SDK] Create Unify Training Client (kubeflow/trainer#1719) by @andreyvelich
- Removing deprecated Job Labels (kubeflow/trainer#1702) by @johnugeorge
- HPA support for PyTorch Elastic (kubeflow/trainer#1701) by @johnugeorge
- [PaddlePaddle] support paddlejob (kubeflow/trainer#1675) by @kuizhiqing
- [SDK] Remove Final Keyword from constants (kubeflow/trainer#1676) by @andreyvelich
- Create TFJob and PyTorchJob from Function APIs in the Training SDK (kubeflow/trainer#1659) by @andreyvelich
- Update training operator sdk version to 1.5.0 (kubeflow/trainer#1651) by @johnugeorge
- Update SDK version to 1.5.0 (kubeflow/trainer#1624) by @johnugeorge
- MXNet SDK with Status check fix (kubeflow/trainer#1618) by @johnugeorge
- Generating MPI python sdk (kubeflow/trainer#1606) by @johnugeorge
- Update k8s dependencies to v0.24.1 (kubeflow/trainer#1604) by @johnugeorge
- Look for fully-qualified job role label in Python sdk (kubeflow/trainer#1588) by @person142
- Migrate test framework to GHA (kubeflow/trainer#1603) by @johnugeorge
- Release Python SDK 1.4.0 (kubeflow/trainer#1541) by @alembiewski
- Extends path in __init__.py for SDK correctly (kubeflow/trainer#1531) by @cakeislife100
- Support elastic training (kubeflow/trainer#1453) by @gaocegege
- Update links and files with the new URL (kubeflow/trainer#1434) by @andreyvelich
- Generate a single `swagger.json` file for all frameworks (kubeflow/trainer#1437) by @alembiewski
- The "follow" of TFJobClient.get_logs (kubeflow/trainer#1254) by @Windfarer
- Move TF Operator e2e tests to AWS Prow (kubeflow/trainer#1204) by @ChanYiLin
- Fix error when `conditions` is empty. (kubeflow/trainer#1185) by @Corea
- Migrate controller implementation to kubeflow/common fashion (kubeflow/trainer#1171) by @ChanYiLin
- Debug sdk test failure (kubeflow/trainer#1143) by @jinchihe
- SDK support getting the TFJob training logs (kubeflow/trainer#1130) by @jinchihe
- Update check status API name (kubeflow/trainer#1117) by @jinchihe
- Enhance tfjobs sdk docs (kubeflow/trainer#1114) by @jinchihe
- Generate TFJob Python SDK (kubeflow/trainer#1103) by @jinchihe
- Init Commit by @andreyvelich

### Fixed
- Use previous stable tag for changelog by @kramaranya
- Update links before SDK release by @kramaranya
- Trainer client backend public by @jaiakash
- Keep the original runtime command in get_runtime_packages() API by @andreyvelich
- Fix __all__ import. by @Electronic-Waste
- Expose BuiltinTrainer API to users by @Electronic-Waste
- Fix bad arg passed to `get_args_using_torchtune_config` (kubeflow/trainer#2647) by @eoinfennessy
- Fix type annotation for `train` method's `trainer` parameter (kubeflow/trainer#2646) by @eoinfennessy
- Add missing import types. (kubeflow/trainer#2566) by @Electronic-Waste
- Using correct entrypoint for mpirun (kubeflow/trainer#2552) by @andreyvelich
- Resolve errors in deserialization (kubeflow/trainer#2457) by @Electronic-Waste
- Add missing retrying package that failed the import (kubeflow/trainer#1439) by @terrytangyuan
- Fix get_logs pod_names type and iteration blocking (kubeflow/trainer#1280) by @Windfarer
- Fix custom_api.delete_namespaced_custom_object args (kubeflow/trainer#1281) by @Windfarer

### Removed
- Remove TrainJobCreated condition (kubeflow/trainer#2621) by @astefanutti
- Remove the Training Operator V1 Source Code (kubeflow/trainer#2389) by @andreyvelich
- Remove support for MXJob (kubeflow/trainer#2150) by @tariq-hasan
- Remove `table-logger` dependency (kubeflow/trainer#1544) by @person142

### New Contributors
* @kramaranya made their first contribution
* @szaher made their first contribution
* @briangallagher made their first contribution
* @wassimbensalem made their first contribution
* @andreyvelich made their first contribution
* @jaiakash made their first contribution
* @astefanutti made their first contribution
* @Electronic-Waste made their first contribution
* @tenzen-y made their first contribution
* @abhijeet-dhumal made their first contribution
* @eoinfennessy made their first contribution
* @Diasker made their first contribution
* @saileshd1402 made their first contribution
* @tarekabouzeid made their first contribution
* @helenxie-bit made their first contribution
* @gavrissh made their first contribution
* @seanlaii made their first contribution
* @Bobbins228 made their first contribution
* @varshaprasad96 made their first contribution
* @sandipanpanda made their first contribution
* @mszadkow made their first contribution
* @Ygnas made their first contribution
* @YosiElias made their first contribution
* @droctothorpe made their first contribution
* @tariq-hasan made their first contribution
* @ChristopheBrown made their first contribution
* @deepanker13 made their first contribution
* @dependabot[bot] made their first contribution
* @garymm made their first contribution
* @johnugeorge made their first contribution
* @kuizhiqing made their first contribution
* @Syulin7 made their first contribution
* @nagar-ajay made their first contribution
* @yaobaiwei made their first contribution
* @person142 made their first contribution
* @alembiewski made their first contribution
* @cakeislife100 made their first contribution
* @gaocegege made their first contribution
* @terrytangyuan made their first contribution
* @Windfarer made their first contribution
* @ChanYiLin made their first contribution
* @Corea made their first contribution
* @jinchihe made their first contribution

[unreleased]: https://github.com/jaiakash/sdk/compare/list...HEAD

<!-- generated by git-cliff -->
