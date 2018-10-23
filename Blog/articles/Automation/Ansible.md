### Anisble

-----

Ansible is an It automation tool which automates the repetitive work and simplifies the work. The main difference between ansible and other automation tools like puppet is it is agent less *(means no software is required to be installed on the client for ansible machine to work)*.Check this page for [installing ansible](http://docs.ansible.com/ansible/latest/intro_installation.html)

#### Inventory

-----------------------------------------------

First thing ever needed for ansible is the hosts file (inventory file). 

  - *Location : /etc/ansible/hosts*
  - *type : INI or yaml*
  - *contains : hosts,host_variables,group of hosts and group_variables*

Example

    [hosts]
    121.10.8.14

    [hosts:vars]
    ansible_user=root
    ansible_ssh_pass=ubuntu

#### Variables

------------------------------------

Here we can mention out the variables in two ways.

 - hosts or inventory file
 - using files to store variables 

Advantage of string variables in files is they can be encoded using the ansible-vault.
The below shows the folder structure t save the variables in files


    ansible/  
    group_vars/
        hosts.json         ## file stores the group variables in json format with group_name as variable_name
    first_playbook.yml   ## playbook to ping the host mentioned in inventory file

This hosts.json can be encrypted using the ansible-vault for storing sensitive information

    ansible-vault encrypt hosts.json


#### Playbooks

----------------------------------------

The playbooks are written in the yaml format. It contains host-groups, hosts, tasks, and handlers.
These all are written using the modules. Example playbook

    ---
    - hosts: gopi
    
    tasks: 
    - name: installing webserver
        yum: name=httpd state=latest
        notify:
        - run apache

    handlers:
    - name: run apache
        service: name=httpd state=restarted

This first_playbook.yml file is saved and ran for pinging the servers using the following command


    ansible-playbook /path_to/first_playbook.yml --ask-vault-pass


Here, if you observe above if we use ansible-vault to encrypt, all the files used in the above playbook should be encrypted with the same password. If we do not encrypt, no need of *--ask-vault-pass* for the command.

#### Output

--------------------------------------------------

    PLAY [hosts] **************************************************************************************************************

    TASK [Gathering Facts] **************************************************************************************************************
    ok: [121.10.8.14]

    TASK [ping hosts server] **************************************************************************************************************
    ok: [121.10.8.14]

    PLAY RECAP **************************************************************************************************************
    121.10.8.14              : ok=2    changed=0    unreachable=0    failed=0
