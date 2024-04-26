# Giza Hackathon — Buenos Aires

## ✨ Open Enrollment Market Forecast

The open enrollment process in the US health insurance  business, presents significant challenges for agents.  One of the main issues is lack of in-advance information about the trendies and expected changes in the market during the following period of registration.   This is the reason why agents need to rely on precise and fast indicators in order to take well-informed and strategic decisions for the open enrollment process.

Having understood this, our proposal focuses on providing one analytic predictive service that utilizes linear regression models on the open enrollment market of consumers prognosis.

To that end, regression models (fed  off public data of the USA Health department and social services) will be developed.  As for the hackathon purposes, models linked to four counties within the state of Florida will be generated  (they are: Bradford Co, Hamilton Co, Levy Co, and Walton Co).  Upon theses counties, two parameters for the algorithm will be used, they are: Fipscod and expected population for 2024 of each county.  Once the parameters are parsed onto the algorithm, users would obtain the expected number of consumers for the next enrollment period for the county being queried.

In summary, agents will be able to rely on a ML solution, with precise prediction of the enrolling number for the next period, which will enable them with the possibility of:

- Better planning their resources and services, by having known the expected demand per county.

- Assigning resources in more effective ways.

- Adapting their marketing strategies to offer a much better service.

With our proposal (and seizing the maturity phase reached by Giza Platform)  we are aiming to open up the possibility of having a conventional-use ML model being displayed on a trustless and verifiable environment.

## ✨ Step-by-Step Guide

- Transpile models to Orion Cairo
```bash
./transpile_files.sh
```

- Deploy an inference endpoints
```bash
# Model name is: bradford_county", model_id-> 522, version_id-> 5
giza endpoints deploy --model-id 522 --version-id 5
# Model name is: hamilton_county, model_id -> 523, version_id -> 6
giza endpoints deploy --model-id 523 --version-id 6
# Model name Model name is: levy_county, model_id -> 525, version_id -> 5
giza endpoints deploy --model-id 525 --version-id 5
# Model name is: walton_county, model_id -> 526, version_id -> 5
giza endpoints deploy --model-id 526 --version-id 5
```

- Run a verifiable inference in AI Actions
First ensure you have an AI Actions workspace created. This step grants access to a user-friendly UI dashboard, enabling you to monitor and manage workflows with ease.
```bash
giza workspaces get
```

- Now let's run a verifiable inference with AI Actions. To design your workflow in AI Actions, you will need to define your task with @task decorator and then action your tasks with @action decorator. You can track the progress of your workflow via the workspace URL previously provided
```bash
#!/bin/bash
python bradford_county.py
🚀 Starting deserialization process...
✅ Deserialization completed! 🎉
21:29:22.058 | INFO    | Task run 'PredictLRBradfordCounty-0' - Finished in state Completed()
21:29:22.064 | INFO    | Action run 'subtle-rottweiler' - Predicted value for input 30010.0 is 1567.955810546875
21:29:22.066 | INFO    | Action run 'subtle-rottweiler' - Proof_id value 0d2a8cfc47f34a3cbbb0af34a569b223
21:29:22.400 | INFO    | Action run 'subtle-rottweiler' - Finished in state Completed()
python hamilton_county.py
🚀 Starting deserialization process...
✅ Deserialization completed! 🎉
21:32:02.904 | INFO    | Task run 'PredictLRHamiltonCounty-0' - Finished in state Completed()
21:32:02.915 | INFO    | Action run 'jovial-oyster' - Predicted value for input 12910.0 is 1059.3804016113281
21:32:02.923 | INFO    | Action run 'jovial-oyster' - Proof_id value 92c3bfc0a07b47c68bab2c5c466a2e74
21:32:03.259 | INFO    | Action run 'jovial-oyster' - Finished in state Completed()
python levy_county.py
🚀 Starting deserialization process...
✅ Deserialization completed! 🎉
21:32:48.750 | INFO    | Task run 'PredictLRLevyCounty-0' - Finished in state Completed()
21:32:48.755 | INFO    | Action run 'radical-jackal' - Predicted value for input 48370.0 is 4103.116638183594
21:32:48.757 | INFO    | Action run 'radical-jackal' - Proof_id value 5a697415e92c4c18877535208c19d586
21:32:49.078 | INFO    | Action run 'radical-jackal' - Finished in state Completed()
```

- Download the proof
```bash
#!/bin/bash
giza endpoints download-proof --endpoint-id 162 --proof-id 0d2a8cfc47f34a3cbbb0af34a569b223 --output-path bradford_county.proof
[giza][2024-04-25 21:45:52.056] Getting proof from endpoint 162 ✅ 
[giza][2024-04-25 21:45:54.691] Proof downloaded to bradford_county.proof ✅ 
giza endpoints download-proof --endpoint-id 163 --proof-id 92c3bfc0a07b47c68bab2c5c466a2e74 --output-path hamilton_county.proof
[giza][2024-04-25 21:46:12.759] Getting proof from endpoint 163 ✅ 
[giza][2024-04-25 21:46:15.360] Proof downloaded to hamilton_county.proof ✅ 
giza endpoints download-proof --endpoint-id 164 --proof-id 5a697415e92c4c18877535208c19d586 --output-path levy_county.proof
[giza][2024-04-25 21:47:40.977] Getting proof from endpoint 164 ✅ 
[giza][2024-04-25 21:47:43.629] Proof downloaded to levy_county.proof ✅ 
giza endpoints download-proof --endpoint-id 165 --proof-id d12346f075e341efbd64c06b7631791c --output-path walton_county.proof
[giza][2024-04-25 21:48:00.881] Getting proof from endpoint 165 ✅ 
[giza][2024-04-25 21:48:06.534] Proof downloaded to walton_county.proof ✅ 
```
- Once the proof is ready, you can download it.
```bash
#!/bin/bash
giza endpoints download-proof --endpoint-id 162 --proof-id 0d2a8cfc47f34a3cbbb0af34a569b223 --output-path bradford_county.proof
[giza][2024-04-25 21:42:26.258] Getting proof from endpoint 162 ✅ 
[giza][2024-04-25 21:42:28.932] Proof downloaded to bradford_county.proof ✅ 
giza endpoints download-proof --endpoint-id 163 --proof-id 92c3bfc0a07b47c68bab2c5c466a2e74 --output-path hamilton_county.proof
[giza][2024-04-25 21:43:05.019] Getting proof from endpoint 163 ✅ 
[giza][2024-04-25 21:43:07.620] Proof downloaded to hamilton_county.proof ✅ 
giza endpoints download-proof --endpoint-id 164 --proof-id 5a697415e92c4c18877535208c19d586 --output-path levy_county.proof
[giza][2024-04-25 21:43:38.751] Getting proof from endpoint 164 ✅ 
[giza][2024-04-25 21:43:42.514] Proof downloaded to levy_county.proof ✅
giza endpoints download-proof --endpoint-id 165 --proof-id d12346f075e341efbd64c06b7631791c --output-path walton_county.proof
[giza][2024-04-25 21:44:08.543] Getting proof from endpoint 165 ✅ 
[giza][2024-04-25 21:44:11.158] Proof downloaded to walton_county.proof ✅ 
```

## 💖 Acknowledgements
We extend our appreciation to the author of the tutorial mentioned below, whose valuable insights and guidance greatly influenced this project.
- [Linear Regression-Giza Actions](https://actions.gizatech.xyz/tutorials/traditional-ml-models-for-zkml/linear-regression)