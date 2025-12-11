# Changelog



### <!-- 0 -->🚀 Features

- Add dependabot to Kubeflow SDK (#194) (kramaranya)

- Update README with announcement blog post (#157) (andreyvelich)

- Add get_best_results API to OptimizerClient (#152) (kramaranya)

- Add local notebook examples to E2E (#149) (Fiona-Waters)

- Add get_job_logs API to OptimizerClient (#148) (kramaranya)

- Add wait_for_job_status and get_best_trial APIs to OptimizerClient (#145) (kramaranya)

- Implement Training Options pattern for flexible TrainJob customization (#91) (abhijeet-dhumal)

- Add ContainerBackend with Docker and Podman (#119) (Fiona-Waters)

- add s3 initializers, add `ignore_patterns` to hf initializers (#131) (rudeigerc)

- add workflow to approve ok-to-test label (#138) (aniketpati1121)

- Add CustomTrainerContainer to create TrainJobs from image (#127) (andreyvelich)

- Hyperparameter Optimization APIs in Kubeflow SDK (#124) (andreyvelich)

- KEP-2655: Support provisioning of cache with Kubeflow SDK (#112) (akshaychitneni)

- Support LoraConfig in TorchTune BuiltinTrainer (#102) (Electronic-Waste)

- KEP-46-Hyperparameter Optimization in Kubeflow SDK (#123) (kramaranya)

- Add automated release CI job (#65) (kramaranya)

- Implement TrainerClient Backends & Local Process (#33) (szaher)

- KEP-2 Local Execution Mode Proposal (#34) (szaher)

- Add support for param unpacking in the training function call (briangallagher)

- Support multiple pip index URLs in CustomTrainer (#79) (wassimbensalem)

- Refactor get_job_logs() API with Iterator (#83) (andreyvelich)

- Implement Kubernetes Backend (#68) (szaher)

- add ROADMAP of Kubeflow SDK (#44) (kramaranya)

- Add `get_runtime_packages()` API (#57) (andreyvelich)

- Support Framework Labels in Runtimes (#56) (andreyvelich)

- Add environment variables argument to CustomTrainer (#54) (astefanutti)

- Add `wait_for_job_status()` API (#52) (andreyvelich)

- Add GitHub action to verify PR titles (#42) (andreyvelich)

- Get namespace from the provided context (kubeflow/trainer#2593) (andreyvelich)

- Support MLX Distributed Runtime with OpenMPI (kubeflow/trainer#2565) (andreyvelich)

- Support DeepSpeed Runtime with OpenMPI (kubeflow/trainer#2559) (andreyvelich)

- Support MPI-based TrainJobs  (kubeflow/trainer#2545) (andreyvelich)

- Refactor the Initializer APIs of TrainJob (kubeflow/trainer#2523) (andreyvelich)

- Migrate to OpenAPI V3 (kubeflow/trainer#2490) (andreyvelich)

- Integrate DependsOn API (kubeflow/trainer#2484) (andreyvelich)

- Generate external Kubernetes and JobSet models (kubeflow/trainer#2466) (andreyvelich)

- Support elastic training (kubeflow/trainer#1453) (gaocegege)


### <!-- 1 -->🐛 Bug Fixes

- Upgrade urllib3 to  v2.6.1 (#193) (Fiona-Waters)

- expose CustomTrainerContainer for import (#185) (AndEsterson)

- update permissions for welcome workflow to avoid 403 error (#181) (aniketpati1121)

- Move permissions to the workflow root (#177) (kramaranya)

- pip install with --user argument fails with image running in python virtual environment (#162) (briangallagher)

- Remove namespace from ClusterTrainingRuntime exception messages (#166) (astefanutti)

- Use PyTorch static rendezvous in container backend (#168) (astefanutti)

- Fix listing containers with Podman backend (#154) (astefanutti)

- Update url for installing docker for use with local notebooks (#151) (Fiona-Waters)

- Remove --user flag from packages install in local subprocess (#147) (andreyvelich)

- Fix empty image for Runtime trainer (#143) (andreyvelich)

- Update Kubeflow SDK diagram (#146) (kramaranya)

- Fix S3 initializer implementation (#144) (andreyvelich)

- Support custom images in ClusterTrainingRuntime for container backend (#140) (Fiona-Waters)

- add --user when install python packages (#136) (briangallagher)

- Fix first-time PR welcome workflow (#117) (kramaranya)

- Skip release workflow on forks (#113) (kramaranya)

- Use previous stable tag for changelog (#103) (kramaranya)

- Update links before SDK release (#98) (kramaranya)

- trainer client backend public (#78) (jaiakash)

- Keep the original runtime command in get_runtime_packages() API (#64) (andreyvelich)

- fix __all__ import. (#43) (Electronic-Waste)

- Expose BuiltinTrainer API to users (#28) (Electronic-Waste)

- Fix bad arg passed to `get_args_using_torchtune_config` (kubeflow/trainer#2647) (eoinfennessy)

- Fix type annotation for `train` method's `trainer` parameter (kubeflow/trainer#2646) (eoinfennessy)

- Add missing import types. (kubeflow/trainer#2566) (Electronic-Waste)

- Using correct entrypoint for mpirun (kubeflow/trainer#2552) (andreyvelich)

- add missing import type Initializer. (kubeflow/trainer#2541) (Electronic-Waste)

- resolve errors in deserialization (kubeflow/trainer#2457) (Electronic-Waste)

- Add missing retrying package that failed the import (kubeflow/trainer#1439) (terrytangyuan)

- fix get_logs pod_names type and iteration blocking (kubeflow/trainer#1280) (Windfarer)

- fix custom_api.delete_namespaced_custom_object args (kubeflow/trainer#1281) (Windfarer)


### <!-- 10 -->💼 Other

- Kubeflow SDK Official Release 0.2.1 (#180) (kramaranya)

- Kubeflow SDK Official Release 0.2.0 (#150) (kramaranya)

- Kubeflow SDK Official Release 0.1.0 (#105) (kramaranya)

- Kubeflow SDK Official Release 0.1.0rc1 (#100) (kramaranya)

- add unit test for trainer sdk (#17) (briangallagher)

- add e2e notebook tests (#27) (briangallagher)

- Update pyproject.toml project links (#40) (szaher)

- Add support for UV & Ruff (#38) (szaher)

- Step down from sdk ownership role (#37) (tenzen-y)

- Add CONTRIBUTING.md (#30) (abhijeet-dhumal)

- Reflect owners updates from KF Trainer (#32) (tenzen-y)

- Consume Trainer models from external package kubeflow_trainer_api (#15) (kramaranya)

- Add pre-commit and flake8 configs (#6) (eoinfennessy)

- Add Stale GitHub action (#7) (kramaranya)

- Move commits from `kubeflow/trainer` (szaher)

- Support mutating dataset preprocessing config in SDK (kubeflow/trainer#2638) (Electronic-Waste)

- Revert "fix(sdk): Fix type annotation for `train` method's `trainer` parameter" (kubeflow/trainer#2651) (Electronic-Waste)

- Move generated Python models into kubeflow_trainer_api package (kubeflow/trainer#2632) (kramaranya)

- Remove TrainJobCreated condition (kubeflow/trainer#2621) (astefanutti)

- Complement torch plugin to support torchtune config mutation (kubeflow/trainer#2587) (Electronic-Waste)

- Add `TorchTuneConfig` to `train()` API (kubeflow/trainer#2522) (Electronic-Waste)

- Fix kubeflow/trainer#2407: Cap nproc_per_node based on CPU resources for PyTorch TrainJob (#2492) (Diasker)

- Refactor current `train()` API (kubeflow/trainer#2513) (Electronic-Waste)

- Implement MPI numProcPerNode defaulter (kubeflow/trainer#2483) (tenzen-y)

- Bump JobSet to v0.8.0 (kubeflow/trainer#2463) (andreyvelich)

- Upgrade jobset SDK version to v0.7.3 (kubeflow/trainer#2445) (Electronic-Waste)

- Add validation to Torch `numProcPerNode` field (kubeflow/trainer#2409) (astefanutti)

- Implement MPI Plugin for Kubeflow Trainer (kubeflow/trainer#2394) (andreyvelich)

- Update the naming conventions for Kubeflow Trainer  (kubeflow/trainer#2415) (andreyvelich)

- Remove the Training Operator V1 Source Code (kubeflow/trainer#2389) (andreyvelich)

- Testing CI in JAX example (kubeflow/trainer#2385) (saileshd1402)

- Fix versions in HuggingFace dataset initializer (kubeflow/trainer#2369) (andreyvelich)

- [SDK] Adding env vars (kubeflow/trainer#2285) (tarekabouzeid)

- Add e2e test for train API (kubeflow/trainer#2199) (helenxie-bit)

- [SDK] Initial implementation of the Kubeflow Training V2 Python SDK (kubeflow/trainer#2324) (andreyvelich)

- Upgrade Kubernetes to v1.31.3 (kubeflow/trainer#2330) (astefanutti)

- Pin accelerate package version in trainer (kubeflow/trainer#2340) (gavrissh)

- Upgrade Kubernetes to v1.30.7 (kubeflow/trainer#2332) (astefanutti)

- [SDK] test: add unit test for get_job_logs method of the training_client (kubeflow/trainer#2275) (seanlaii)

- [SDK] Use torchrun to create PyTorchJob from function (kubeflow/trainer#2276) (andreyvelich)

- [SDK] test: add unit test for list_jobs method of the training_client (kubeflow/trainer#2267) (seanlaii)

- [SDK] Training Client Conditions related unit tests (kubeflow/trainer#2253) (Bobbins228)

- [SDK] Minor fix in wait_for_job_conditions with job_kind python training API (kubeflow/trainer#2265) (saileshd1402)

- [SDK] move env var to constants.py (kubeflow/trainer#2268) (varshaprasad96)

- Update JAX image to use image published by Kubeflow  (kubeflow/trainer#2264) (sandipanpanda)

- Add JAX controller (kubeflow/trainer#2194) (sandipanpanda)

- [SDK] Allow customising base trainer and storage images in Train API (kubeflow/trainer#2261) (varshaprasad96)

- [Feature] Support managed by external controller (kubeflow/trainer#2203) (mszadkow)

- Bump Training Python SDK to 1.8.1 version (kubeflow/trainer#2257) (andreyvelich)

- [SDK] Read namespace from the current context (kubeflow/trainer#2255) (andreyvelich)

- [SDK] Fix typo of "get_pvc_spec" (kubeflow/trainer#2250) (helenxie-bit)

- [SDK] test: add unit test for get_job method of the training_client (kubeflow/trainer#2205) (Bobbins228)

- [SDK] test: add unit tests for delete_job() method (kubeflow/trainer#2232) (Bobbins228)

- [SDK] Add UTs for `wait_for_job_conditions` (kubeflow/trainer#2196) (Electronic-Waste)

- [SDK] Fix trainer error: Update the version of base image and add "num_labels" for downloading pretrained models (kubeflow/trainer#2230) (helenxie-bit)

- Change isort profile to black for full compatibility (kubeflow/trainer#2234) (Ygnas)

- [SDK] Unit tests for TrainingClient APIs - get_job_pod_names and update_job (kubeflow/trainer#2192) (YosiElias)

- Enhance pre-commit hooks with flake8 linting (kubeflow/trainer#2195) (Ygnas)

- Update trainer to ensure type consistency for `train_args` and `lora_config` (kubeflow/trainer#2181) (helenxie-bit)

- Update the name of PVC in `train` API (kubeflow/trainer#2187) (helenxie-bit)

- Implement pre-commit hooks (kubeflow/trainer#2184) (droctothorpe)

- Update `huggingface_hub` Version in the storage initializer to fix ImportError (kubeflow/trainer#2180) (helenxie-bit)

- Add JAX API (kubeflow/trainer#2163) (sandipanpanda)

- Remove support for MXJob (kubeflow/trainer#2150) (vector-flow)

- [SDK] Add more unit tests for TrainingClient APIs - get_job_pods (kubeflow/trainer#2175) (YosiElias)

- Bump Training Python SDK to 1.8.0 version (kubeflow/trainer#2172) (andreyvelich)

- [SDK] Fix Failed condition in wait Job API (kubeflow/trainer#2160) (andreyvelich)

- [SDK] Sync Transformers version for train API (kubeflow/trainer#2146) (andreyvelich)

- [SDK] Explain Python version support cycle (kubeflow/trainer#2144) (andreyvelich)

- Update Slack Invitation (kubeflow/trainer#2142) (andreyvelich)

- [SDK] Fix Incorrect Events in get_job_logs API (kubeflow/trainer#2122) (andreyvelich)

- changed package name to flake8 to fix pytests pip install (kubeflow/trainer#2109) (ChristopheBrown)

- Support Python 3.11 and Drop Python 3.7 (kubeflow/trainer#2105) (tenzen-y)

- Replace outdated images with latest ones (kubeflow/trainer#2083) (tenzen-y)

- [SDK] Add docstring for Train API (kubeflow/trainer#2075) (andreyvelich)

- Upgrade the minimum required Kubernetes version to v1.27.2 (kubeflow/trainer#2066) (tenzen-y)

- adding fine tune example with s3 as the dataset store (kubeflow/trainer#2006) (deepanker13)

- Bump transformers from 4.37.2 to 4.38.0 in /sdk/python/kubeflow/storage_initializer (kubeflow/trainer#2056) (dependabot[bot])

- Bump transformers from 4.37.2 to 4.38.0 in /sdk/python/kubeflow/trainer (kubeflow/trainer#2055) (dependabot[bot])

- Bump black from 21.12b0 to 24.3.0 in /sdk/python (kubeflow/trainer#2033) (dependabot[bot])

- Modify LLM Trainer to support BERT and Tiny LLaMA (kubeflow/trainer#2031) (andreyvelich)

- Add Fine-Tune BERT LLM Example (kubeflow/trainer#2021) (andreyvelich)

- Fix URL in python SDK setup.py (kubeflow/trainer#2011) (garymm)

- [SDK] Add resources per worker for Create Job API (kubeflow/trainer#1990) (andreyvelich)

- [SDK] Fix Worker and Master templates for PyTorchJob (kubeflow/trainer#1988) (andreyvelich)

- publish trainer hugging face image (kubeflow/trainer#1985) (deepanker13)

- Adding Training image needed for train api (kubeflow/trainer#1963) (deepanker13)

- Add test to create PyTorchJob from func (kubeflow/trainer#1979) (andreyvelich)

- [SDK] Get Kubernetes Events for Job (kubeflow/trainer#1975) (andreyvelich)

- [SDK] Train API (kubeflow/trainer#1962) (deepanker13)

- [SDK] Add information about TrainingClient logging (kubeflow/trainer#1973) (andreyvelich)

- Train api dataset download changes (kubeflow/trainer#1959) (deepanker13)

- Train api init container creation (kubeflow/trainer#1958) (deepanker13)

- utils changes needed to add train api (kubeflow/trainer#1954) (deepanker13)

- Training operator SDK unit test (kubeflow/trainer#1938) (deepanker13)

- Avoid modifying log level globally (kubeflow/trainer#1944) (droctothorpe)

- Merge v1.7 branch changes to Main (kubeflow/trainer#1940) (johnugeorge)

- Use a community hosted image in MXJob E2E (kubeflow/trainer#1928) (tenzen-y)

- Replace XGBoost image for E2E with community hosted (kubeflow/trainer#1922) (tenzen-y)

- [SDK] Consolidate Naming for CRUD APIs (kubeflow/trainer#1907) (andreyvelich)

- Implement suspend semantics (kubeflow/trainer#1859) (tenzen-y)

- Make Condition and ReplicaStatus optional (kubeflow/trainer#1862) (tenzen-y)

- Set correct ENV for PytorchJob to support torchrun (kubeflow/trainer#1840) (kuizhiqing)

- Add check pods are not scheduled when testing gang-scheduler integrations in e2e (kubeflow/trainer#1835) (tenzen-y)

- Merge kubeflow/common to training-operator (kubeflow/trainer#1813) (johnugeorge)

- Make scheduler-plugins the default gang scheduler. (kubeflow/trainer#1747) (Syulin7)

- Improve E2E tests for the gang-scheduling (kubeflow/trainer#1801) (tenzen-y)

- make timeout configurable from e2e tests (kubeflow/trainer#1787) (nagar-ajay)

- Containerize e2e tests for training operator conformance (kubeflow/trainer#1780) (nagar-ajay)

- Disable istio-sidecar injection (kubeflow/trainer#1778) (nagar-ajay)

- E2e test in k8s cluster and Namespace option (kubeflow/trainer#1774) (nagar-ajay)

- Fix XGBoost flaky e2e tests (kubeflow/trainer#1775) (nagar-ajay)

- [Bugfix][SDK] pod has no metadata attr anymore in the get_job_logs() … (kubeflow/trainer#1760) (yaobaiwei)

- [SDK] Use Training Client without Kube Config (kubeflow/trainer#1740) (andreyvelich)

- Add E2E test for gang-scheduling (kubeflow/trainer#1736) (tenzen-y)

- Adopting coschduling plugin (kubeflow/trainer#1724) (tenzen-y)

- [SDK] Create Unify Training Client (kubeflow/trainer#1719) (andreyvelich)

- Removing deprecated Job Labels (kubeflow/trainer#1702) (johnugeorge)

- HPA support for PyTorch Elastic (kubeflow/trainer#1701) (johnugeorge)

- [PaddlePaddle] support paddlejob (kubeflow/trainer#1675) (kuizhiqing)

- [SDK] Remove Final Keyword from constants (kubeflow/trainer#1676) (andreyvelich)

- Create TFJob and PyTorchJob from Function APIs in the Training SDK (kubeflow/trainer#1659) (andreyvelich)

- Update training operator sdk version to 1.5.0 (kubeflow/trainer#1651) (johnugeorge)

- Update SDK version to 1.5.0 (kubeflow/trainer#1624) (johnugeorge)

- MXNet SDK with Status check fix (kubeflow/trainer#1618) (johnugeorge)

- Add clientset for MPIJob, PytorchJob, MXJob, and XGBoostJob (kubeflow/trainer#1610) (tenzen-y)

- Adding MPI python sdk (kubeflow/trainer#1608) (johnugeorge)

- Adding XGboost Python sdk  (kubeflow/trainer#1607) (johnugeorge)

- Generating MPI python sdk (kubeflow/trainer#1606) (johnugeorge)

- Update k8s dependencies to v0.24.1 (kubeflow/trainer#1604) (johnugeorge)

- Look for fully-qualified job role label in Python sdk (kubeflow/trainer#1588) (person142)

- Migrate test framework to GHA (kubeflow/trainer#1603) (johnugeorge)

- Remove `table-logger` dependency (kubeflow/trainer#1544) (person142)

- Release Python SDK 1.4.0 (kubeflow/trainer#1541) (alembiewski)

- extends path in __init__.py for SDK correctly (kubeflow/trainer#1531) (cakeislife100)

- Update links and files with the new URL (kubeflow/trainer#1434) (andreyvelich)

- Generate a single `swagger.json` file for all frameworks (kubeflow/trainer#1437) (alembiewski)

- Add Python SDK for Kubeflow Training Operator (kubeflow/trainer#1420) (alembiewski)

- the "follow" of TFJobClient.get_logs (kubeflow/trainer#1254) (Windfarer)

- Move TF Operator e2e tests to AWS Prow (kubeflow/trainer#1204) (ChanYiLin)

- Fix error when `conditions` is empty. (kubeflow/trainer#1185) (Corea)

- Migrate controller implementation to kubeflow/common fashion (kubeflow/trainer#1171) (ChanYiLin)

- Debug sdk test failure (kubeflow/trainer#1143) (jinchihe)

- SDK support getting the TFJob training logs (kubeflow/trainer#1130) (jinchihe)

- Add watch function for TFJob python Client API (kubeflow/trainer#1122) (jinchihe)

- Update check status API name (kubeflow/trainer#1117) (jinchihe)

- add API to wait for TFJob done (kubeflow/trainer#1116) (jinchihe)

- Enhance tfjobs sdk docs (kubeflow/trainer#1114) (jinchihe)

- generate TFJob Python SDK (kubeflow/trainer#1103) (jinchihe)

- Add GitHub issue and PR templates (#5) (eoinfennessy)

- Init Commit (andreyvelich)


### <!-- 7 -->⚙️ Miscellaneous Tasks

- bump actions/github-script from 7 to 8 (#201) (dependabot[bot])

- bump actions/download-artifact from 4 to 6 (#200) (dependabot[bot])

- bump actions/stale from 5 to 10 (#199) (dependabot[bot])

- bump actions/setup-python from 5 to 6 (#198) (dependabot[bot])

- bump actions/checkout from 4 to 6 (#202) (dependabot[bot])

- Add new items to the roadmap (#187) (kramaranya)

- Add HPO support to readme and SDK diagram (#141) (kramaranya)

- Add pre-commit configuration and CI workflow (#134) (aniketpati1121)

- added AGENTS.MD (#106) (hawkaii)

- Add Spark Operator to the future supported projects (#109) (andreyvelich)

- Ignore PRs titles with area/release labels in CI (#101) (kramaranya)

- Add proper ruff configuration (#69) (szaher)

- Update CONTRIBUTING.md to use uv (#41) (szaher)

- Add welcome new contributors CI (#82) (kramaranya)

- Use explicit exception chaining (#80) (andreyvelich)

- Nominate @kramaranya and @szaher as Kubeflow SDK reviewers (#76) (andreyvelich)

- Enable parallel builds for coveralls (#81) (kramaranya)

- Remove tool.hatch.build.targets from pyproject (#73) (kramaranya)

- Move dev extras to dependency-groups (#71) (kramaranya)

- Update README.md (#67) (kramaranya)

- move pyproject.toml to root (#61) (kramaranya)

- Align Kubernetes versions from Trainer for e2e tests (#58) (astefanutti)

- Add dev tests with master dependencies (#55) (kramaranya)

- Add Coveralls Badge to the README (#53) (andreyvelich)

- Remove accelerator label from the runtimes (#51) (andreyvelich)

- Add E2E tests for Kubeflow Trainer (kubeflow/trainer#2470) (andreyvelich)



### New Contributors
* @dependabot[bot] made their first contribution
* @kramaranya made their first contribution
* @Fiona-Waters made their first contribution
* @AndEsterson made their first contribution
* @aniketpati1121 made their first contribution
* @briangallagher made their first contribution
* @astefanutti made their first contribution
* @andreyvelich made their first contribution
* @abhijeet-dhumal made their first contribution
* @rudeigerc made their first contribution
* @hawkaii made their first contribution
* @akshaychitneni made their first contribution
* @Electronic-Waste made their first contribution
* @szaher made their first contribution
* @wassimbensalem made their first contribution
* @jaiakash made their first contribution
* @tenzen-y made their first contribution
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
* @vector-flow made their first contribution
* @ChristopheBrown made their first contribution
* @deepanker13 made their first contribution
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

