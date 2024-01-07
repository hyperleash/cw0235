# Distributed Analysis System Setup Guide

This guide outlines the steps required to set up a distributed analysis system for proteome analysis using Ansible. 
The setup process involves preparing the control node, preparing the necessary SSH keys, cloning the repository, and running the analysis pipeline.

## Step 1: Connect to the Control Node

Make sure you have the lecturer key used during the cluster creating. Then use the following command:
```bash
ssh -i path/to/key ec2-user@ec2-35-178-42-199.eu-west-2.compute.amazonaws.com
```

## Step 2: Copy the private lecturer key to the control node
This is required so that the control node can access the workers

```bash
scp path/to/lecturer_key ec2-user@ec2-35-178-42-199.eu-west-2.compute.amazonaws.com:~/.ssh/lecturer_key
```

## Step 3: Install the required packages onto the control node
This installs python, pip, git, and ansible onto the control node

```bash
sudo yum update -y

sudo yum install -y python3 git

sudo yum install -y python3-pip

sudo pip3 install ansible

sudo pip3 install pandas
```

## Step 4: Clone the coursework github repository
To clone the repository and put all of the required code on the control node run this command:
```bash
git clone https://github.com/hyperleash/cw0235.git
```

## Step 4.5: (Optional) Create and distribute a new key pair
To improve security you can run the key_exchange.yml playbook to create and distribute a new key pair.

```bash
cd cw0235
ansible-playbook --private-key=~/.ssh/lecturer_key -i hosts key_exchange.yml
```

## Step 5: Run the pipeline
Before running the pipeline, put the ids you want to analyse to the experiment_ids.txt file

You can run the distributed analysis using this command:
```bash
cd cw0235
ansible-playbook --private-key=~/.ssh/lecturer_key -i hosts distribute_pipeline.yml
```

If you did step 4.5 replace the private key with ~/.ssh/ansible_identity

## Step 6: Get results
Once the pipeline finishes, results will be stored in these files in cw0235 directory:

- best_hits.csv
- stats.csv

