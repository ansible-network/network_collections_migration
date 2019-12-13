network_collections_migration
=============================

This project used the
https://github.com/ansible-community/collection_migration to migrate
collection content from ansibe/ansible into ansible-network specific
collections.

Adding a new job
----------------

We'll be adding a zuul job to migrate content to the following fake
collection:

  https://github.com/ansible-network/ansible_collection.example.fake

In this case, then collection namespace is 'example' and the name is 'fake'.

Create Zuul job
---------------

First edit the .zuul.yaml file in this folder, adding the following 2 jobs:


    - job:
        name: propose-network-collections-migration-example-fake
        parent: propose-network-collections-migration-base
        required-projects:
          - name: github.com/ansible-network/ansible_collections.example.fake
        vars:
          ansible_collection_namespace: example
          ansible_collection_name: fake
          proposal_project_src: ~/src/github.com/ansible-network/ansible_collections.example.fake

    - job:
        name: network-collections-migration-example-fake
        parent: network-collections-migration-base
        required-projects:
          - name: github.com/ansible-network/ansible_collections.example.fake
        vars:
          ansible_collection_namespace: example
          ansible_collection_name: fake

The network-collection-migration-example-fake jobs runs in both the check /
gate pipelines to validate we can create the content properly.  Where the
propose-network-collections-migration-example-fake jobs, run in the post /
periodic pipelines to create new PRs if needed against:

  https://github.com/ansible-network/ansible_collection.example.fake

While still editing .zuul.yaml add the jobs to the pipelines:

    - project-template:
        name: network-collections-migration
        description: |
          A common set of migration jobs used by ansible network team
        check:
          jobs:
            - network-collections-migration-example-fake
        gate:
          queue: network-collections-migration
          jobs:
            - network-collections-migration-example-fake
        periodic:
          jobs:
            - propose-network-collections-migration-example-fake
        post:
          jobs:
            - propose-network-collections-migration-example-fake

Save and close the file.

Next, create scenarios/example/fake/example.yml with content to migrate:

    fake:
      module_utils:
      - network/fake/*
      modules:
      - network/fake/*
      action:
      - fake.py
      cliconf:
      - fake.py
      doc_fragments:
      - fake.py
      httpapi:
      - fake.py
      terminal:
      - fake.py

Save and close file.

Lastly, create symlink to ansible.netcommon from scenarios/example/fake:

  ln -s ../../ansible/netcommon/ansible.yml .

Finally create a PR to github, to preform code review.

If successful, once the PR is merged, the network-collections-migration-example-fake
job will run and open a PR againt the collection.  This will then trigger the
next step of tests to be run.
