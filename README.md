# text_mining_prep
UPDATE Aug. 26, 2025: The code provided here has been merged into our primary [CatMiner repository](https://github.com/benjww/CatMiner/) following the release of updates to the [ChemDataExtractor2 package](https://github.com/CambridgeMolecularEngineering/chemdataextractor2/tree/master) that have advanced the range of Python versions supported. This repository is now deprecated and will no longer be updated. 

Distributed as part of the publication "Use of Large Language Models for Extracting and Analyzing Data from Heterogeneous Catalysis Literature" by Benjamin W. Walls and Suljo Linic.

This repository contains code used to obtain bulk lists of DOIs, download associated papers in markup language (i.e., HTML or XML) format, and convert them to plain text. This is necessary to obtain the text files that we use as inputs for our text mining tool [CatMiner](https://github.com/benjww/CatMiner/), but should be useful for other text mining tools as well. We have only confirmed support for Python 3.7 in macOS. In the future we hope to support 3.8+ and merge this code base into the linked CatMiner repository. 

Please install required packages by running "pip install requirements.txt" before you begin. 

If you find our code or workflow to be useful, please cite the corresponding publication:

1. Walls, B. W.; Linic, S. Use of Large Language Models for Extracting and Analyzing Data from Heterogeneous Catalysis Literature. ACS Catal. 2025, 14751–14763. https://doi.org/10.1021/acscatal.5c03844.
