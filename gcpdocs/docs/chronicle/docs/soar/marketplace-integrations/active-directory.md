---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/active-directory/
title: Integrate Active Directory with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:58:39.399697+00:00
---

# Integrate Active Directory with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/active-directory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Active Directory with Google SecOps

This document explains how to integrate Active Directory with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/ActiveDirectory.zip).

## Use cases

The **Active Directory** integration uses Google SecOps capabilities to support the following use cases:

  * **Activate and deactivate users:** Deactivate a potentially compromised user account and prevent further unauthorized access.

  * **Reset passwords:** Automatically reset the user password in Active Directory and notify the user of the change.

  * **Manage groups:** Add new users to the appropriate security groups based on their role and make sure that the users have the correct access permissions.

  * **Retrieve user information:** Retrieve user details such as group memberships, last login time, and contact information about a specific user account.

  * **Automate offboarding:** Disable accounts, remove them from groups, and transfer file ownership when an employee offboards.




## Before you begin

Before you configure the **Active Directory** integration in Google SecOps, verify that your network environment, Active Directory Domain Services (AD DS), and service account credentials satisfy all operational prerequisites.

To prepare your environment for integration, complete the following prerequisites:

  1. Verify network connectivity and DNS resolution between your Google SecOps instance (or Remote Agent) and your Active Directory Domain Controllers.

  2. Optional: If connecting over LDAPS (port 636, required for password resets) using an internal Certificate Authority, configure the CA certificate by encoding your root or intermediate certificate into a base64 string.

  3. Create a dedicated Active Directory service account adhering to the Principle of Least Privilege.

  4. Review the required action permissions to determine the attributes and access rights needed for the specific actions you plan to run.

  5. Delegate permissions on target Organizational Units for the actions you plan to use (using Active Directory Users and Computers or PowerShell and dsacls), making sure the service account has explicit Read and Write access to the `userAccountControl` attribute.




### Network and DNS requirements

Google SecOps communicates directly with Active Directory Domain Controllers using the Lightweight Directory Access Protocol (LDAP or LDAPS) over TCP.

Make sure your network environment meets the following connectivity rules:

  * **Port connectivity** : Make sure your network firewalls and routing allow outbound communication from Google SecOps (or your Remote Agent) to your Active Directory Domain Controllers on the following ports:

    * **LDAP (standard)** : Open port `389/TCP` for unencrypted LDAP communication.
    * **LDAPS (recommended - mandatory for passwords)** : Open port `636/TCP` (or your custom SSL/TLS port). LDAPS is required for encrypted directory traffic and is mandatory for password modification actions.
  * **DNS and hostname resolution** : Active Directory requires accurate hostname resolution to match SSL/TLS certificates and directory service bindings. If your domain is resolved by a fully qualified DNS name through your internal DNS setup, no additional host configuration is needed. If DNS resolution isn't available on your remote agent container image, configure the `/etc/hosts` file.




#### Configure the `/etc/hosts` file

This configuration is optional. If your domain controller is already resolved through your internal DNS setup, skip this section. If your remote agent can't resolve the Active Directory domain controller using DNS, map the host manually in the `/etc/hosts` file to match SSL/TLS certificates and directory service bindings.

To configure the `/etc/hosts` file, complete the following steps:

  1. Open `/etc/hosts` in a text editor with administrative privileges:
         
         sudo vi /etc/hosts
         

  2. Add an entry mapping the domain controller's IP address to its fully qualified domain name (FQDN):
         
         192.0.2.195 dc01.example.local
         

  3. Save and close the file.




If you don't need a CA certificate for the integration, proceed to configuring the authentication and service account requirements. Otherwise, configure your CA certificate.

### Configure the CA certificate

This step is optional. If you connect using standard LDAP (port 389) or use a publicly trusted certificate, skip this section and proceed to Authentication and service account requirements. If you connect over LDAPS (port 636, required for password resets) using a certificate issued by a private or internal CA, provide the base64-encoded certificate string during setup to establish a trusted TLS connection.

To configure and upload the CA certificate, complete the following steps:

  1. Encode your PEM-formatted certificate file:

     * **Linux** : `bash base64 -w 0 mycert.crt`

     * **macOS** : `bash base64 -i mycert.crt`

  2. Copy the full output string (including encoded headers) and paste it into the **CA Certificate File - parsed into Base64 String** field in the Google SecOps integration configuration.

  3. Set the **Server** parameter to the FQDN of the domain controller (not its IP address) so the hostname matches the Common Name (CN) or Subject Alternative Name (SAN) on the certificate.

  4. Click **Test** to validate the TLS handshake.




### Authentication and service account requirements

The **Active Directory** integration authenticates using standard AD DS credentials.

Make sure your authentication setup complies with the following security practices:

  * **Dedicated service account** : Create a dedicated service account (such as `svc_secops_ad`) specifically for Google SecOps automated playbooks. Avoid using interactive user accounts or built-in domain administrator accounts.

  * **Username format** : The username can be provided as a User Principal Name (UPN) (such as `svc_secops@example.local`) or as a Down-Level Logon Name (`EXAMPLE\svc_secops`).

  * **PoLP** : Don't add the service account to privileged built-in groups such as **Domain Admins** , **Enterprise Admins** , or **Account Operators**. Instead, grant granular permissions on specific OUs where user, computer, or group objects reside.




### Configure action permissions (least privilege)

Grant the authenticating service account only the Active Directory permissions and LDAP attribute access required for the specific actions you plan to run.

**Important:** Status-checking and lifecycle actions (including **Enable Account** , **Disable Account** , **Enable Computer** , **Disable Computer** , and **Enrich Entities**) require explicit Read Property and Write Property rights on the `userAccountControl` attribute. 

If the service account can't read `userAccountControl`, Active Directory omits the attribute entirely from LDAP responses. In Google SecOps, this produces unhandled null exceptions (such as `TypeError: 'NoneType' object is not subscriptable`). Make sure this attribute is delegated explicitly on all target OUs.

Refer to the minimal permissions for Active Directory actions in the following table:

Action Name | Required AD DS Permission / Extended Right | Target Object Class | Description / Attribute Scope  
---|---|---|---  
**Ping** | `Read Property` | User, Domain Root | Queries the configured service account object (`sAMAccountName`, `userPrincipalName`, `mail`) to validate directory connectivity and credentials.  
**Enrich Entities** | 

  * `List Contents`
  * `Read Property` (target attributes: `userAccountControl`, `sAMAccountName`, `mail`, `memberOf`, `lockoutTime`, `pwdLastSet`)

| User, Computer, Group | Queries user and computer attributes and resolves nested group memberships. Requires `Read Property` on `userAccountControl` to prevent null subscript errors.  
**Disable Account** | 

  * `Read Property`: `userAccountControl`
  * `Write Property`: `userAccountControl`

| User | Reads and sets the `ACCOUNTDISABLE` flag (`0x0002`) on the target user object.  
**Enable Account** | 

  * `Read Property`: `userAccountControl`
  * `Write Property`: `userAccountControl`

| User | Reads and clears the `ACCOUNTDISABLE` flag (`0x0002`) on the target user object.  
**Disable Computer** | 

  * `Read Property`: `userAccountControl`
  * `Write Property`: `userAccountControl`

| Computer | Reads and sets the `ACCOUNTDISABLE` flag on the target computer object.  
**Enable Computer** | 

  * `Read Property`: `userAccountControl`
  * `Write Property`: `userAccountControl`

| Computer | Reads and clears the `ACCOUNTDISABLE` flag on the target computer object.  
**Release Locked Account** | 

  * `Read Property`: `lockoutTime`
  * `Write Property`: `lockoutTime`

| User | Reads and sets the `lockoutTime` attribute to `0` to unlock a locked user account.  
**Force Password Update** | 

  * `Read Property`: `pwdLastSet`
  * `Write Property`: `pwdLastSet`

| User | Reads and sets the `pwdLastSet` attribute to `0` to require the user to change their password at next sign-in.  
**Set User Password** | 

  * Extended Right: `Reset Password` (`User-Force-Change-Password`)
  * (Optional) `Write Property`: `unicodePwd`

| User | Resets the target user's password. Requires LDAPS (port 636) or StartTLS.  
**Add User To Group** | 

  * `Read Property`: `member`
  * `Write Property`: `member`

| Group | Adds the target user's Distinguished Name (`distinguishedName`) to the group's `member` attribute.  
**Remove User From Group** | 

  * `Read Property`: `member`
  * `Write Property`: `member`

| Group | Removes the target user's Distinguished Name (`distinguishedName`) from the group's `member` attribute.  
**Change User OU** | 

  * `Delete Child Object` (User) on source OU
  * `Create Child Object` (User) on destination OU
  * `Write Property`: `name`, `distinguishedName`

| Organizational Unit, User | Moves user objects between OUs using LDAP `modify_dn`.  
**Change Host OU** | 

  * `Delete Child Object` (Computer) on source OU
  * `Create Child Object` (Computer) on destination OU
  * `Write Property`: `name`, `distinguishedName`

| Organizational Unit, Computer | Moves computer objects between OUs using LDAP `modify_dn`.  
**Update attributes of an AD User** | `Write Property` on target attributes (such as `mail`, `title`, `department`, `telephoneNumber`, `description`, or `manager`) | User | Modifies specified attribute values on the target user object.  
**Update attributes of an AD Host** | `Write Property` on target attributes (such as `description` or `location`) | Computer | Modifies specified attribute values on the target computer object.  
**Get Group Members** | 

  * `List Contents`
  * `Read Property`: `member`, `sAMAccountName`, `distinguishedName`

| Group, User, Computer | Queries group membership and member account attributes.  
**Get Manager Contact Details** | 

  * `Read Property`: `manager`
  * `Read Property`: `cn`, `telephoneNumber`, `mail`, `displayName`, `title`

| User | Reads the `manager` attribute from the target user object and retrieves the manager's contact details.  
**Is User In Group** | 

  * `Read Property`: `memberOf`, `sAMAccountName`

| User, Group | Evaluates whether a user account belongs to the specified security or distribution group.  
**List User Groups** | 

  * `Read Property`: `memberOf`, `sAMAccountName`

| User, Group | Returns the list of all groups assigned to the specified user account.  
**Search Active Directory** | 

  * `List Contents`
  * `Read Property` on queried attributes

| User, Computer, Group, Organizational Unit | Executes custom LDAP filter queries against the directory subtree.  
  
### Delegating permissions in Active Directory

To enforce the PoLP without granting broad administrative rights, delegate permissions on target OUs using either the graphical ADUC console or the PowerShell and dsacls command-line tools. You only need to use one of these methods, and you only need to delegate the permissions required for the specific actions you plan to run.

#### Delegate control using ADUC

If you prefer using a graphical interface, use the Delegation of Control Wizard in ADUC to delegate object and property-specific permissions.

Run the wizard on the target OU to grant the object and property permissions required for the actions you plan to use (such as reading and writing account control flags, resetting passwords, or unlocking accounts).

For step-by-step guidance on running the wizard, see the Microsoft documentation on [Delegation of Control in AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegation-control-wizard).

#### Delegate control using PowerShell and dsacls

If you prefer a command-line approach or want to automate permission assignments, use PowerShell with the built-in `dsacls.exe` utility instead of ADUC.

Run only the command examples that apply to the actions you plan to use on an administrative workstation or Domain Controller, substituting your target OU and service account name:

  * Grant Read and Write permissions on `userAccountControl` for user objects (to enable or disable user accounts and prevent enrichment errors): `powershell dsacls.exe "OU=Users,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:RPWP;userAccountControl;user"`
  * Grant Read and Write permissions on `userAccountControl` for computer objects (to enable or disable computers): `powershell dsacls.exe "OU=Computers,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:RPWP;userAccountControl;computer"`
  * Grant unlock account permissions (`lockoutTime`): `powershell dsacls.exe "OU=Users,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:RPWP;lockoutTime;user"`
  * Grant force password change permissions (`pwdLastSet`): `powershell dsacls.exe "OU=Users,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:RPWP;pwdLastSet;user"`
  * Grant password reset rights (`Reset Password` extended right): `powershell dsacls.exe "OU=Users,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:CA;Reset Password;user"`
  * Grant membership modification rights on a security group: `powershell dsacls.exe "CN=SecOps-Quarantine,OU=Groups,DC=example,DC=local" /G "EXAMPLE\svc_secops_ad:RPWP;member;group"`



For more details on syntax and parameter switches, see the Microsoft documentation on [dsacls](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771151\(v=ws.11\)).

**Note:** In Active Directory, members of protected administrative groups have inheritance disabled by the internal AdminSDHolder process. Delegated permissions assigned at an OU level won't apply to protected administrative accounts. 

For more information on managing protected objects, see the Microsoft documentation on [AdminSDHolder and Protected Accounts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-c--protected-accounts-and-groups-in-active-directory).

## Integration parameters

The **Active Directory** integration requires the following parameters:

Parameter | Description  
---|---  
`Server` | Required. The hostname, DNS name, or IP address of the Active Directory server. The integration communicates using the LDAP protocol. To use a custom port, append it to the address (such as `mydomain.com:636`). By default, the integration uses port 636 when SSL/TLS is enabled and port 389 when it's disabled.  
`Username` | Required. The username or email address of the user to connect to Active Directory, such as `DOMAIN\username` or `user@example.com`. This parameter also accepts the `userPrincipalName` attribute.  
`Password` | Required.The password for the user account.  
`Domain` | Required. The full DNS path to your domain within the network namespace. Provide the fully qualified domain name (FQDN) of your domain in the following format: `SUBDOMAIN.ROOT_DOMAIN`. For example, if your internal Active Directory domain is `example.local`, the FQDN to enter is `example.local`. If your internal Active Directory domain is `corp.example.com`, the FQDN to enter is `corp.example.com`.  
`Custom Query Fields` | Optional. A comma-separated list of custom Active Directory fields to include in queries, such as `customField1, customField2`.  
`CA Certificate File - parsed into Base64 String` | Optional. The CA certificate file string encoded into the base64 format obtained when configuring the CA certificate. Provide the full value.  
`Use SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Active Directory server and uses secure LDAPS (port 636). If not selected, it uses standard LDAP (port 389).  
`Debug Logging` | Optional. If selected, the integration logs detailed debug information for Active Directory operations.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from your workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Run a manual action in your case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case#run-manual-action). 

### Add User To Group

Use the **Add User To Group** action to add users from the case to one or more Active Directory groups, such as adding an account to a restricted access group during an investigation. The action automatically identifies the target users from the case and adds them to the specified groups.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Add User To Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Name` | Required. A comma-separated list of groups to add users to.  
  
#### Action outputs

The **Add User To Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add User To Group** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added the following users to the group "GROUP_NAME" in Active Directory: ENTITY_ID` `The following users were already a part of the group "GROUP_NAME" in Active Directory: ENTITY_ID` | The action succeeded.  
`Action wasn't able to add the following users to the group "GROUP_NAME" in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the service account has permission to modify the `member` attribute on the target group.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and that the entity identifiers match valid usernames or email addresses.  
`The following groups were not found in Active Directory: GROUP_NAME` | The action failed for the specified groups.Check the spelling of the group names in the `Group Name` parameter and confirm that the groups exist in the configured domain.  
`No users were added to the group "GROUP_NAME" in Active Directory.` | The action failed for the specified group.Verify that the target users exist in Active Directory and that the service account has write access to the specified group.  
`No users were added to the provided groups in Active Directory.` | The action failed.Confirm that the case contains valid `User` entities and that the specified groups exist in Active Directory.  
`Error executing action "Add User To Group". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, input parameters, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add User To Group** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Change Host OU

Use the **Change Host OU** action to move computers in the case to a different Organizational Unit in Active Directory, such as moving a compromised machine to a quarantine OU with restricted policies. The action automatically identifies the target computers from the case and moves them to the specified destination OU.

This action runs on the Google SecOps `Hostname` entity.

#### Action inputs

The **Change Host OU** action requires the following parameters:

Parameter | Description  
---|---  
`OU Name` | Required. The name of the new host OU.  
  
#### Action outputs

The **Change Host OU** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Change Host OU** action can return the following output messages:

Output message | Message description  
---|---  
`Changed OU for the following hosts: ENTITY_ID` | The action succeeded.  
`Failed to change OU for the following hosts : ENTITY_ID` | The action failed for the specified hosts.Verify that the destination OU exists and that the service account has permission to move computer objects between the source and destination OUs.  
`The following hosts were not found in Active Directory: ENTITY_ID` | The action failed for the specified hosts.Verify that the computer accounts exist in Active Directory and match the `Hostname` entities in the case.  
`The action didn't change OU on any hosts.` | The action failed.Check that the target computers and the destination OU exist in Active Directory and that the service account has permissions to move the computer accounts.  
`Error executing action "Change Host OU". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, the `OU Name` parameter, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Change Host OU** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Change User OU

Use the **Change User OU** action to move users in the case to a different Organizational Unit in Active Directory, such as moving an account to a restricted OU during an incident or offboarding workflow. The action automatically identifies the target users from the case and moves them to the specified destination OU.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Change User OU** action requires the following parameters:

Parameter | Description  
---|---  
`OU Name` | Required. The name of the new user OU.  
  
#### Action outputs

The **Change User OU** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Change User OU** action can return the following output messages:

Output message | Message description  
---|---  
`Changed OU for the following users: ENTITY_ID` | The action succeeded.  
`Failed to change OU for the following users : ENTITY_ID` | The action failed for the specified users.Verify that the destination OU exists and that the service account has permission to move user objects between the source and destination OUs.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`The action didn't change OU on any users.` | The action failed.Check that the target users and the destination OU exist in Active Directory and that the service account has permissions to move the user accounts.  
`Error executing action "Change User OU". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, the `OU Name` parameter, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Change User OU** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Disable Account

Use the **Disable Account** action to deactivate user accounts in Active Directory. This action automatically targets the users attached to the case.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Disable Account** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Disable Account** action can return the following output messages:

Output message | Message description  
---|---  
`Disabled account for the following users: ENTITY_ID` | The action succeeded.  
`Failed to disable account for the following users: ENTITY_ID` | The action failed for the specified users.Verify that the service account has read and write permissions for the `userAccountControl` attribute on the target user accounts and that the users aren't protected administrative accounts.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`No users were disabled in Active Directory.` | The action failed.Confirm that the case contains valid `User` entities and that the service account has permission to disable the target accounts.  
`Error executing action "Disable Account". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Disable Account** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Disable Computer

Use the **Disable Computer** action to deactivate computer accounts in Active Directory to prevent compromised or unauthorized machines from authenticating to the domain. The action automatically targets the hostnames attached to the case.

This action runs on the Google SecOps `Hostname` entity.

#### Action inputs

None.

#### Action outputs

The **Disable Computer** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Disable Computer** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully disabled the following computers in Active Directory: ENTITY_ID` `The following computers were already disabled in Active Directory: ENTITY_ID` | The action succeeded.  
`Action wasn't able to disable the following computers in Active Directory: ENTITY_ID` | The action failed for the specified computers.Verify that the service account has read and write permissions for the `userAccountControl` attribute on the target computer objects.  
`The following computers were not found in Active Directory: ENTITY_ID` | The action failed for the specified computers.Verify that the computer accounts exist in Active Directory and match the `Hostname` entities in the case.  
`No computers were disabled in Active Directory.` | The action failed.Confirm that the case contains valid `Hostname` entities and that the service account has permission to disable the target computer accounts.  
`Error executing action "Disable Computer". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Disable Computer** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enable Account

Use the **Enable Account** action to re-enable disabled user accounts in Active Directory. The action automatically targets the users attached to the case.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Enable Account** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Enable Account** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enabled the following users in Active Directory: ENTITY_ID` `The following users were already enabled in Active Directory: ENTITY_ID` | The action succeeded.  
`Action wasn't able to enable the following users in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the service account has read and write permissions for the `userAccountControl` attribute on the target user accounts.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`No users were enabled in Active Directory.` | The action failed.Confirm that the case contains valid `User` entities and that the service account has permission to enable the target accounts.  
`Error executing action "Enable Account". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enable Account** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enable Computer

Use the **Enable Computer** action to re-enable disabled computer accounts in Active Directory so the machines can authenticate to the domain again. The action automatically targets the hostnames attached to the case.

This action runs on the Google SecOps `Hostname` entity.

#### Action inputs

None.

#### Action outputs

The **Enable Computer** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Enable Computer** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enabled the following computers in Active Directory: ENTITY_ID` `The following computers were already enabled in Active Directory: ENTITY_ID` | The action succeeded.  
`Action wasn't able to enable the following computers in Active Directory: ENTITY_ID` | The action failed for the specified computers.Verify that the service account has read and write permissions for the `userAccountControl` attribute on the target computer objects.  
`The following computers were not found in Active Directory: ENTITY_ID` | The action failed for the specified computers.Verify that the computer accounts exist in Active Directory and match the `Hostname` entities in the case.  
`No computers were enabled in Active Directory.` | The action failed.Confirm that the case contains valid `Hostname` entities and that the service account has permission to enable the target computer accounts.  
`Error executing action "Enable Computer". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enable Computer** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich Entities

Use the **Enrich Entities** action to retrieve Active Directory profile details, account status, and group memberships for users and computers in the case. You can enrich entities with all available directory information or limit the results and case wall table to specific attributes.

This action is asynchronous. Adjust the script timeout value in the Google SecOps IDE for the action, if needed.

The **Enrich Entities** action runs on the following Google SecOps entities:

  * `User`
  * `Hostname`



#### Action inputs

The **Enrich Entities** action requires the following parameters:

Parameter | Description  
---|---  
`Mark Entities as Internal` | Optional. If selected, the action automatically marks the successfully enriched entities as internal entities. Enabled by default.  
`Create Case Wall Table` | Optional. If selected, the action generates a case wall table containing the retrieved Active Directory attributes for each enriched entity. Enabled by default.  
`Specific Attribute Names To Enrich With` | Optional. A comma-separated list of attribute names to enrich the entities with. If you don't provide any value, the action enriches entities with all available attributes. If an attribute contains multiple values, the action enriches the attribute with all available values. This parameter is case-sensitive.  
`Should Case Wall Table be filtered by the specified Attributes?` | Optional. If selected, the action populates the case wall table only with attributes specified in `Specific Attribute Names To Enrich With`.  
`Should JSON result be filtered by the specified Attributes?` | Optional. If selected, the JSON result returns only attributes specified in `Specific Attribute Names To Enrich With`.  
  
#### Action outputs

The **Enrich Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Enrich Entities** action provides the following table on the **Case Wall** when `Create Case Wall Table` is selected:

  * **Table name** : `Report for: <var class="readonly">ENTITY_ID</var>`
  * **Columns** : Active Directory attribute names and values retrieved for the entity (or filtered by the `Specific Attribute Names To Enrich With` parameter if `Should Case Wall Table be filtered by the specified Attributes?` is selected).



##### Entity enrichment

The **Enrich Entities** action supports the following entity enrichment:

Enrichment field name | Logic  
---|---  
`AD_primaryGroupID` | The action returns the value if it exists in the JSON result.  
`AD_logonCount` | The action returns the value if it exists in the JSON result.  
`AD_cn` | The action returns the value if it exists in the JSON result.  
`AD_countryCode` | The action returns the value if it exists in the JSON result.  
`AD_objectClass` | The action returns the value if it exists in the JSON result.  
`AD_userPrincipalName` | The action returns the value if it exists in the JSON result.  
`AD_adminCount` | The action returns the value if it exists in the JSON result.  
`AD_lastLogonTimestamp` | The action returns the value if it exists in the JSON result.  
`AD_manager` | The action returns the value if it exists in the JSON result.  
`AD_instanceType` | The action returns the value if it exists in the JSON result.  
`AD_distinguishedName` | The action returns the value if it exists in the JSON result.  
`AD_dSCorePropagationData` | The action returns the value if it exists in the JSON result.  
`AD_msDS-SupportedEncryptionTypes` | The action returns the value if it exists in the JSON result.  
`AD_objectSid` | The action returns the value if it exists in the JSON result.  
`AD_whenCreated` | The action returns the value if it exists in the JSON result.  
`AD_uSNCreated` | The action returns the value if it exists in the JSON result.  
`AD_lockoutTime` | The action returns the value if it exists in the JSON result.  
`AD_badPasswordTime` | The action returns the value if it exists in the JSON result.  
`AD_pwdLastSet` | The action returns the value if it exists in the JSON result.  
`AD_sAMAccountName` | The action returns the value if it exists in the JSON result.  
`AD_objectCategory` | The action returns the value if it exists in the JSON result.  
`AD_lastLogon` | The action returns the value if it exists in the JSON result.  
`AD_objectGUID` | The action returns the value if it exists in the JSON result.  
`AD_whenChanged` | The action returns the value if it exists in the JSON result.  
`AD_badPwdCount` | The action returns the value if it exists in the JSON result.  
`AD_accountExpires` | The action returns the value if it exists in the JSON result.  
`AD_displayName` | The action returns the value if it exists in the JSON result.  
`AD_name` | The action returns the value if it exists in the JSON result.  
`AD_memberOf` | The action returns the value if it exists in the JSON result.  
`AD_codePage` | The action returns the value if it exists in the JSON result.  
`AD_userAccountControl` | The action returns the value if it exists in the JSON result.  
`AD_sAMAccountType` | The action returns the value if it exists in the JSON result.  
`AD_uSNChanged` | The action returns the value if it exists in the JSON result.  
`AD_sn` | The action returns the value if it exists in the JSON result.  
`AD_givenName` | The action returns the value if it exists in the JSON result.  
`AD_lastLogoff` | The action returns the value if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich Entities** action:
    
    
    [
        {
            "EntityResult": {
                "primaryGroupID": [513],
                "logonCount": [6505],
                "cn": ["user name"],
                "countryCode": [0],
                "objectClass": ["top", "person", "organizationalPerson"],
                "userPrincipalName": ["user@example.com"],
                "adminCount": [1],
                "lastLogonTimestamp": ["2019-01-09 08:42:03.540783+00:00"],
                "manager": ["CN=user name,OU=R&D,OU=TLV,OU=host name,DC=domain,DC=LOCAL"],
                "instanceType": [4],
                "distinguishedName": ["CN=user name,OU=R&D,OU=TLV,OU=host,DC=domain,DC=LOCAL"],
                "dSCorePropagationData": ["2019-01-14 14:39:16+00:00"],
                "msDS-SupportedEncryptionTypes": [0],
                "objectSid": ["ID"],
                "whenCreated": ["2011-11-07 08:00:44+00:00"],
                "uSNCreated": [7288202],
                "lockoutTime": ["1601-01-01 00:00:00+00:00"],
                "badPasswordTime": ["date"],
                "pwdLastSet": ["date"],
                "sAMAccountName": ["example"],
                "objectCategory": ["CN=Person,CN=Schema,CN=Configuration,DC=host,DC=LOCAL"],
                "lastLogon": ["2019-01-14 17:13:54.463070+00:00"],
                "objectGUID": ["GUID"],
                "whenChanged": ["2019-01-14 16:49:01+00:00"],
                "badPwdCount": [1],
                "accountExpires": ["9999-12-31 23:59:59.999999"],
                "displayName": ["example user"],
                "name": ["user"],
                "memberOf": ["CN=\\\\u05e7\\\\u05d1\\\\u05d5\\\\u05e6\\\\u05d4 \\\\u05d1\\\\u05e2\\\\u05d1\\\\u05e8\\\\u05d9\\\\u05ea,OU=TEST,OU=QA,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL", "CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=domain,DC=LOCAL", "CN=Local Admin,OU=Groups,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL"],
                "codePage": [0],
                "userAccountControl": [111],
                "sAMAccountType": [805306368],
                "uSNChanged": [15301168],
                "sn": ["example"],
                "givenName": ["user"],
                "lastLogoff": ["1601-01-01 00:00:00+00:00"]
            },
            "Entity": "user@example.com"
        }
    ]
    

##### Output messages

The **Enrich Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Active Directory Permalink: SERVER` `Enriched the following Users ENTITY_ID` `Enriched the following Hosts ENTITY_ID` `All entities were enriched.` | The action succeeded.  
`The following entities were not found in Active Directory: ENTITY_ID` | The action failed for the specified entities.Verify that the user or host accounts exist in Active Directory and match the entity identifiers in the case.  
`Failed to enrich the following Users ENTITY_ID` | The action failed for the specified users.Verify that the service account has permission to read attributes (including `userAccountControl`) on the target user accounts and check that any custom attributes exist in Active Directory.  
`Failed to enrich the following Hosts ENTITY_ID` | The action failed for the specified hosts.Verify that the service account has permission to read attributes (including `userAccountControl`) on the target computer accounts and check that any custom attributes exist in Active Directory.  
`No entities were enriched.` | The action failed.Confirm that the case contains valid `User` or `Hostname` entities that exist in Active Directory.  
`Error executing action "Enrich Entities". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, custom query fields, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Entities** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Force Password Update

Use the **Force Password Update** action to require users to change their password the next time they sign in. The action automatically targets the users attached to the case.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Force Password Update** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Force Password Update** action can return the following output messages:

Output message | Message description  
---|---  
`Forced password update on next logon for the following users: ENTITY_ID` | The action succeeded.  
`Failed to force password update on next logon for the following users: ENTITY_ID` | The action failed for the specified users.Verify that the service account has read and write permissions for the `pwdLastSet` attribute on the target user accounts.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`Password update wasn't forced on any users.` | The action failed.Confirm that the case contains valid `User` entities and that the service account has permission to update password expiration settings.  
`Error executing action "Force Password Update". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Force Password Update** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Group Members

Use the **Get Group Members** action to list the users, computers, or both that belong to a specific Active Directory group. You can optionally narrow the search to a specific Organizational Unit or parent group and include members from nested subgroups.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Group Members** action requires the following parameters:

Parameter | Description  
---|---  
`Group Name` | Required. The name of the group that contains the listed members.  
`Members Type` | Required. The member type to retrieve from the group. The possible values are as follows:

  * `Only Users`
  * `Only Hosts`
  * `Both`

The default value is `Only Users`.  
`Where To Search` | Required. A specific `Organizational Unit` or `Group` to scope the search to. The possible values are as follows:

  * `Select Option`
  * `Organizational Unit`
  * `Group`

The default value is `Select Option`.  
`Filter Object Value` | Optional. The name of the `Organizational Unit` or `Group` where the action searches for the target group. This parameter is required if `Where To Search` is set to `Organizational Unit` or `Group`.  
`Perform Nested Search` | Optional. If selected, the action retrieves members from nested subgroups that belong to the target group.  
`Limit` | Optional. The maximum number of listings to retrieve from Active Directory. The default value is `100`.  
  
#### Action outputs

The **Get Group Members** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Group Members** action provides the following table on the **Case Wall** :

  * **Table name** : `Members of Active Directory group: <var class="readonly">GROUP_NAME</var>`
  * **Columns** : 
    * `Distinguished Name`
    * `SAM Account Name`
    * `User Principal Name`
    * `Type`



##### JSON result

The following example shows the JSON result output received when using the **Get Group Members** action:
    
    
    [
      {
        "dn": "CN=Example User1,OU=User Accounts,DC=example,DC=local",
        "sAMAccountName": "ExampleUser1",
        "userPrincipalName": "user1@example.local",
        "type": "CN=Person,CN=Schema,CN=Configuration,DC=example,DC=local"
      },
      {
        "dn": "CN=Example User2,CN=Users,DC=example,DC=local",
        "sAMAccountName": "ExampleUser2",
        "userPrincipalName": "user2@example.local",
        "type": "CN=Person,CN=Schema,CN=Configuration,DC=example,DC=local"
      }
    ]
    

##### Output messages

The **Get Group Members** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved members of the group "GROUP_NAME" from Active Directory.` `Group "GROUP_NAME" doesn't contain any members matching search criteria in Active Directory.` | The action succeeded.  
`Error executing action "Get Group Members". Reason: Filter Object Value should be provided` | The action failed.Provide a valid OU or group name in the `Filter Object Value` parameter when `Where To Search` is set to `Organizational Unit` or `Group`.  
`Error executing action "Get Group Members". Reason: Given value for Limit should be a positive number.` | The action failed.Enter a whole number greater than `0` in the `Limit` parameter.  
`Error executing action "Get Group Members". Reason: Given group doesn't exist in Active Directory.` | The action failed.Check the group name in the `Group Name` parameter and confirm that the group exists within the configured search scope.  
`Error executing action "Get Group Members". Reason: Specified Organizational Unit doesn't exist in Active Directory.` | The action failed.Verify that the Organizational Unit specified in `Filter Object Value` exists in Active Directory.  
`Error executing action "Get Group Members". Reason: Specified Group in "Filter Object Value" doesn't exist in Active Directory.` | The action failed.Verify that the parent group specified in `Filter Object Value` exists in Active Directory.  
`Error executing action "Get Group Members". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, input parameters, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Group Members** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Manager Contact Details

Use the **Get Manager Contact Details** action to look up the manager of a user in Active Directory and retrieve the manager's contact information. The action automatically targets the users attached to the case.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Get Manager Contact Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Manager Contact Details** action provides the following table on the **Case Wall** :

  * **Table name** : `Manager Contact: <var class="readonly">ENTITY_ID</var>`
  * **Columns** : 
    * `Manager Name`
    * `Manager Phone`



##### Entity enrichment

The **Get Manager Contact Details** action supports the following entity enrichment:

Enrichment field name | Logic  
---|---  
`AD_Manager_Name` | The action returns the value if it exists in the JSON result.  
`AD_Manager_phone` | The action returns the value if it exists in the JSON result.  
`AD_primaryGroupID` | The action returns the value if it exists in the JSON result.  
`AD_logonCount` | The action returns the value if it exists in the JSON result.  
`AD_cn` | The action returns the value if it exists in the JSON result.  
`AD_countryCode` | The action returns the value if it exists in the JSON result.  
`AD_objectClass` | The action returns the value if it exists in the JSON result.  
`AD_userPrincipalName` | The action returns the value if it exists in the JSON result.  
`AD_adminCount` | The action returns the value if it exists in the JSON result.  
`AD_lastLogonTimestamp` | The action returns the value if it exists in the JSON result.  
`AD_manager` | The action returns the value if it exists in the JSON result.  
`AD_instanceType` | The action returns the value if it exists in the JSON result.  
`AD_distinguishedName` | The action returns the value if it exists in the JSON result.  
`AD_dSCorePropagationData` | The action returns the value if it exists in the JSON result.  
`AD_msDS-SupportedEncryptionTypes` | The action returns the value if it exists in the JSON result.  
`AD_objectSid` | The action returns the value if it exists in the JSON result.  
`AD_whenCreated` | The action returns the value if it exists in the JSON result.  
`AD_uSNCreated` | The action returns the value if it exists in the JSON result.  
`AD_lockoutTime` | The action returns the value if it exists in the JSON result.  
`AD_badPasswordTime` | The action returns the value if it exists in the JSON result.  
`AD_pwdLastSet` | The action returns the value if it exists in the JSON result.  
`AD_sAMAccountName` | The action returns the value if it exists in the JSON result.  
`AD_objectCategory` | The action returns the value if it exists in the JSON result.  
`AD_lastLogon` | The action returns the value if it exists in the JSON result.  
`AD_objectGUID` | The action returns the value if it exists in the JSON result.  
`AD_whenChanged` | The action returns the value if it exists in the JSON result.  
`AD_badPwdCount` | The action returns the value if it exists in the JSON result.  
`AD_accountExpires` | The action returns the value if it exists in the JSON result.  
`AD_displayName` | The action returns the value if it exists in the JSON result.  
`AD_name` | The action returns the value if it exists in the JSON result.  
`AD_memberOf` | The action returns the value if it exists in the JSON result.  
`AD_codePage` | The action returns the value if it exists in the JSON result.  
`AD_userAccountControl` | The action returns the value if it exists in the JSON result.  
`AD_sAMAccountType` | The action returns the value if it exists in the JSON result.  
`AD_uSNChanged` | The action returns the value if it exists in the JSON result.  
`AD_sn` | The action returns the value if it exists in the JSON result.  
`AD_givenName` | The action returns the value if it exists in the JSON result.  
`AD_lastLogoff` | The action returns the value if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Manager Contact Details** action:
    
    
    [
       {
            "EntityResult":
            {
                "primaryGroupID": [513],
                "logonCount": [6505],
                "cn": ["user name"],
                "countryCode": [0],
                "objectClass": ["top", "person", "organizationalPerson"],
                "userPrincipalName": ["user@example.com"],
                "adminCount": [1],
                "lastLogonTimestamp": ["2019-01-09 08:42:03.540783+00:00"],
                "manager": ["CN=user name,OU=R&D,OU=TLV,OU=host name,DC=domain,DC=LOCAL"],
                "instanceType": [4],
                "distinguishedName": ["CN=user name,OU=R&D,OU=TLV,OU=host,DC=domain,DC=LOCAL"],
                "dSCorePropagationData": ["2019-01-14 14:39:16+00:00"],
                "msDS-SupportedEncryptionTypes": [0],
                "objectSid": ["ID"],
                "whenCreated": ["2011-11-07 08:00:44+00:00"],
                "uSNCreated": [7288202],
                "lockoutTime": ["1601-01-01 00:00:00+00:00"],
                "badPasswordTime": ["date"],
                "pwdLastSet": ["date"],
                "sAMAccountName": ["example"],
                "objectCategory": ["CN=Person,CN=Schema,CN=Configuration,DC=host,DC=LOCAL"],
                "lastLogon": ["2019-01-14 17:13:54.463070+00:00"],
                "objectGUID": ["GUID"],
                "whenChanged": ["2019-01-14 16:49:01+00:00"],
                "badPwdCount": [1],
                "accountExpires": ["9999-12-31 23:59:59.999999"],
                "displayName": ["example"],
                "name": ["user"],
                "memberOf": ["CN=\\\\u05e7\\\\u05d1\\\\u05d5\\\\u05e6\\\\u05d4 \\\\u05d1\\\\u05e2\\\\u05d1\\\\u05e8\\\\u05d9\\\\u05ea,OU=TEST,OU=QA,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL", "CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=domain,DC=LOCAL", "CN=Local Admin,OU=Groups,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL"],
                "codePage": [0],
                "userAccountControl": [111],
                "sAMAccountType": [805306368],
                "uSNChanged": [15301168],
                "sn": ["example"],
                "givenName": ["user"],
                "lastLogoff": ["1601-01-01 00:00:00+00:00"]
            },
            "Entity": "user@example.com"
        }
    ]
    

##### Output messages

The **Get Manager Contact Details** action can return the following output messages:

Output message | Message description  
---|---  
`Retrieved manager details for the following users: ENTITY_ID` | The action succeeded.  
`The following users don't have managers specified in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the `manager` attribute is populated on the target user accounts in Active Directory.  
`Failed to retrieve manager details for the following users: ENTITY_ID` | The action failed for the specified users.Verify that the service account has permission to read the `manager` attribute and the manager's user profile in Active Directory.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`No manager details were retrieved for the provided users.` | The action failed.Confirm that the case contains valid `User` entities that have a manager assigned in Active Directory.  
`Error executing action "Get Manager Contact Details". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Manager Contact Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Is User In Group

Use the **Is User In Group** action to check whether specific users belong to a given Active Directory group. By default, the action checks the `User` entities in the case, or you can enter a comma-separated list of usernames in the `User Name` parameter to check specific accounts directly.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Is User In Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Name` | Required. The group name to check, such as `administrators`.  
`User Name` | Optional. A comma-separated list of usernames to check. If you don't provide a value, the action checks the `User` entities in the case.  
`Where To Search` | Required. A specific `Organizational Unit` or `Group` to scope the search to. The possible values are as follows:

  * `Select Option`
  * `Organizational Unit`
  * `Group`

The default value is `Select Option`.  
`Filter Object Value` | Optional.The name of the `Organizational Unit` or `Group` where the action searches for the target group. This parameter is required if `Where To Search` is set to `Organizational Unit` or `Group`.  
`Search In Subgroups` | Optional.If selected, the action searches recursively within nested subgroups.  
  
#### Action outputs

The **Is User In Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Is User In Group** action:
    
    
    [
        {
            "EntityResult": true,
            "Entity": "USER1@EXAMPLE.COM"
        }, {
            "EntityResult": false,
            "Entity": "USER2@EXAMPLE.COM"
        }, {
            "EntityResult": true,
            "Entity": "USER3@EXAMPLE.COM"
        }
    ]
    

##### Output messages

The **Is User In Group** action can return the following output messages:

Output message | Message description  
---|---  
`USER_NAME IN GROUP_NAME;` `USER_NAME NOT in GROUP_NAME;` | The action succeeded.  
`The following users were not found in Active Directory: USER_NAME` | The action failed for the specified users.Verify that the usernames or `User` entities exist in Active Directory.  
`None of the provided users were found in Active Directory.` | The action failed.Confirm that the case contains valid `User` entities or that the usernames specified in the `User Name` parameter exist in Active Directory.  
`Error executing action "Is User In Group". Reason: Filter Object Value should be provided` | The action failed.Provide a valid OU or group name in the `Filter Object Value` parameter when `Where To Search` is set to `Organizational Unit` or `Group`.  
`Error executing action "Is User In Group". Reason: Given group doesn't exist in Active Directory.` | The action failed.Check the group name in the `Group Name` parameter and confirm that the group exists within the configured search scope.  
`Error executing action "Is User In Group". Reason: Specified Organizational Unit doesn't exist in Active Directory.` | The action failed.Verify that the Organizational Unit specified in `Filter Object Value` exists in Active Directory.  
`Error executing action "Is User In Group". Reason: Specified Group in "Filter Object Value" doesn't exist in Active Directory.` | The action failed.Verify that the parent group specified in `Filter Object Value` exists in Active Directory.  
`Error executing action "Is User In Group". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, input parameters, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Is User In Group** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List User Groups

Use the **List User Groups** action to retrieve a list of all Active Directory groups that a user belongs to. The action automatically targets the users attached to the case.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **List User Groups** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **List User Groups** action:
    
    
    [
        {
            "EntityResult": ["Domain Users"],
            "Entity": "user@example.com"
        }
    ]
    

##### Output messages

The **List User Groups** action can return the following output messages:

Output message | Message description  
---|---  
`Groups were listed for the following users: ENTITY_ID` | The action succeeded.  
`No groups were found for the following users: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts are assigned to at least one explicit group in the `memberOf` attribute in Active Directory.  
`Failed to list groups for the following users: ENTITY_ID` | The action failed for the specified users.Verify that the service account has permission to read the `memberOf` attribute on the target user accounts.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`No groups were listed.` | The action failed.Confirm that the case contains valid `User` entities that belong to groups in Active Directory.  
`Error executing action "List User Groups". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List User Groups** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to verify that Google SecOps can connect and authenticate to your Active Directory server using the configured integration settings.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Connected successfully.` | The action succeeded.  
`Error executing action "Ping". Reason: ERROR_REASON` | The action failed.Check the server address, port, SSL settings, or service account credentials in the integration configuration.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Release Locked Account

Use the **Release Locked Account** action to unlock user accounts in Active Directory that were locked out after too many failed sign-in attempts. The action automatically targets the users attached to the case.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Release Locked Account** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Release Locked Account** action can return the following output messages:

Output message | Message description  
---|---  
`Unlocked account for the following users: ENTITY_ID` | The action succeeded.  
`Failed to unlock account for the following users: ENTITY_ID` | The action failed for the specified users.Verify that the service account has read and write permissions for the `lockoutTime` attribute on the target user accounts.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`No accounts were unlocked.` | The action failed.Confirm that the case contains valid `User` entities and that the service account has permission to unlock the target accounts.  
`Error executing action "Release Locked Account". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Release Locked Account** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove User From Group

Use the **Remove User From Group** action to remove users in the case from one or more Active Directory groups, such as revoking elevated group access during an incident. The action automatically identifies the target users from the case and removes them from the specified groups.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Remove User From Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Name` | Required. A comma-separated list of groups to remove the users from.  
  
#### Action outputs

The **Remove User From Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Remove User From Group** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully removed the following users from the group "GROUP_NAME" in Active Directory: ENTITY_ID` `The following users were not a part of the group "GROUP_NAME" in Active Directory: ENTITY_ID` | The action succeeded.  
`Action wasn't able to remove the following users from the group "GROUP_NAME" in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the service account has permission to modify the `member` attribute on the target group.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`The following groups were not found in Active Directory: GROUP_NAME` | The action failed for the specified groups.Check the spelling of the group names in the `Group Name` parameter and confirm that the groups exist in the configured domain.  
`No users were removed from the group "GROUP_NAME" in Active Directory. ` | The action failed for the specified group.Verify that the target users exist in Active Directory and that the service account has write access to the specified group.  
`No users were removed from the provided groups in Active Directory.` | The action failed.Confirm that the case contains valid `User` entities and that the specified groups exist in Active Directory.  
`Error executing action "Remove User From Group". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, input parameters, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove User From Group** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Search Active Directory

Use the **Search Active Directory** action to search your directory for users, computers, groups, or Organizational Units using built-in search conditions or a custom query. You can also filter the search by specific Organizational Units and choose which directory fields to include in the results.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search Active Directory** action requires the following parameters:

Parameter | Description  
---|---  
`Search Condition` | Required. The condition to apply to the search. The possible values are as follows:

  * `Contains`
  * `Exact Match`
  * `Starts With`
  * `Custom LDAP Query`

The default value is `Contains`.  
`Include Domain` | Optional. If selected, the action includes the domain component when searching with the `Contains`, `Exact Match`, or `Starts With` conditions.  
`Search Object` | Required. An object type to search for when not using `Custom LDAP Query`. The possible values are as follows:

  * `Select Option`
  * `User`
  * `Host`
  * `Group`
  * `Organizational Unit`

The default value is `Select Option`.  
`Filter Object Value` | Required. An object value to filter by, or the full LDAP query string when `Search Condition` is set to `Custom LDAP Query`.  
`Custom Fields` | Optional. A comma-separated list of LDAP attributes to return in the search results.  
`Specific OUs to Search` | Optional. A comma-separated list of Organizational Unit names to restrict the search scope.  
`Include Default Search Fields` | Optional. If selected, the action includes default Active Directory fields in the returned results in addition to any specified `Custom Fields`. Enabled by default.  
`Max Records To Return` | Optional. A maximum number of records to retrieve from Active Directory. The default value is `100`.  
`Sort Field` | Optional. An LDAP attribute name used to sort the returned entries.  
  
#### Action outputs

The **Search Active Directory** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Search Active Directory** action provides the following table on the **Case Wall** :

  * **Table name** : `Active Directory Search Results`
  * **Columns** : Active Directory attributes returned for the matching directory entries (based on `Include Default Search Fields` and `Custom Fields`).



##### JSON result

The following example shows the JSON result output received when using the **Search Active Directory** action:
    
    
    [
          {
            "primaryGroupID": [
              513
            ],
            "logonCount": [
              6505
            ],
            "cn": [
              "user name"
            ],
            "countryCode": [
              0
            ],
            "objectClass": [
              "top",
              "person",
              "organizationalPerson"
            ],
            "userPrincipalName": [
              "user@example.com"
            ],
            "adminCount": [
              1
            ],
            "lastLogonTimestamp": [
              "2019-01-09 08:42:03.540783+00:00"
            ],
            "manager": [
              "CN=user name,OU=R&D,OU=TLV,OU=host name,DC=domain,DC=LOCAL"
            ],
            "instanceType": [
              4
            ],
            "distinguishedName": [
              "CN=user name,OU=R&D,OU=TLV,OU=host,DC=domain,DC=LOCAL"
            ],
            "dSCorePropagationData": [
              "2019-01-14 14:39:16+00:00"
            ],
            "msDS-SupportedEncryptionTypes": [
              0
            ],
            "objectSid": [
              "ID"
            ],
            "whenCreated": [
              "2011-11-07 08:00:44+00:00"
            ],
            "uSNCreated": [
              7288202
            ],
            "lockoutTime": [
              "1601-01-01 00:00:00+00:00"
            ],
            "badPasswordTime": [
              "date"
            ],
            "pwdLastSet": [
              "date"
            ],
            "sAMAccountName": [
              "example"
            ],
            "objectCategory": [
              "CN=Person,CN=Schema,CN=Configuration,DC=host,DC=LOCAL"
            ],
            "lastLogon": [
              "2019-01-14 17:13:54.463070+00:00"
            ],
            "objectGUID": [
              "GUID"
            ],
            "whenChanged": [
              "2019-01-14 16:49:01+00:00"
            ],
            "badPwdCount": [
              1
            ],
            "accountExpires": [
              "9999-12-31 23:59:59.999999"
            ],
            "displayName": [
              "example"
            ],
            "name": [
              "user"
            ],
            "memberOf": [
              "CN=\\\\u05e7\\\\u05d1\\\\u05d5\\\\u05e6\\\\u05d4 \\\\u05d1\\\\u05e2\\\\u05d1\\\\u05e8\\\\u05d9\\\\u05ea,OU=TEST,OU=QA,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL",
              "CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=domain,DC=LOCAL",
              "CN=Local Admin,OU=Groups,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL"
            ],
            "codePage": [
              0
            ],
            "userAccountControl": [
              111
            ],
            "sAMAccountType": [
              805306368
            ],
            "uSNChanged": [
              15301168
            ],
            "sn": [
              "example"
            ],
            "givenName": [
              "user"
            ],
            "lastLogoff": [
              "1601-01-01 00:00:00+00:00"
            ]
          }
        ]
    

##### Output messages

The **Search Active Directory** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully performed the query "QUERY_STRING" in Active Directory.` `No results to show following the query: "QUERY_STRING".` | The action succeeded.  
`Error executing action "Search Active Directory". Reason: you need to select "Search Object" or choose "Custom LDAP Query" as a "Search Condition"` | The action failed.Select a valid object type in the `Search Object` parameter or change `Search Condition` to `Custom LDAP Query`.  
`Error executing action "Search Active Directory". Reason: Value for the parameter "Max Records To Return" should be a positive number.` | The action failed.Enter a whole number greater than `0` in the `Max Records To Return` parameter.  
`Error executing action "Search Active Directory". Reason: The following OUs were not found in Active Directory: OU_NAMES` | The action failed.Check the spelling of the Organizational Units in the `Specific OUs to Search` parameter and confirm that they exist in Active Directory.  
`Error executing action "Search Active Directory". Reason: Knowingly invalid query was executed: "QUERY_STRING". Please verify the inputs and try again.` | The action failed.Check the syntax of your custom query or filter value in the `Filter Object Value` parameter and verify that any specified `Custom Fields` or `Sort Field` names are valid LDAP attributes.  
`Error executing action "Search Active Directory". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, input parameters, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Active Directory** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Set User Password

Use the **Set User Password** action to reset the password for users in the case to a new password. Make sure the integration is connected over SSL (LDAPS) and that the new password meets your domain's password complexity rules.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Set User Password** action requires the following parameters:

Parameter | Description  
---|---  
`New Password` | Required. The new password value.  
  
#### Action outputs

The **Set User Password** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Set User Password** action can return the following output messages:

Output message | Message description  
---|---  
`Reset password for the following users: ENTITY_ID` | The action succeeded.  
`Failed to reset password for the following users: ENTITY_ID` | The action failed for the specified users.Verify that the new password meets domain password complexity and history requirements and that the target users aren't protected administrative accounts.  
`The following users were not found in Active Directory: ENTITY_ID` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`No passwords were changed.` | The action failed.Confirm that the case contains valid `User` entities and that the service account has permission to reset passwords on the target accounts.  
`Failed to execute "Set User Password" action! Watch Over Extended Rights permission or SSL connection.` | The action failed.Make sure `Use SSL` is selected in the integration configuration (LDAPS on port `636`) and that the service account has the **Reset Password** extended right.  
`Error executing action "Set User Password". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, input parameters, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set User Password** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Update attributes of an AD Host

Use the **Update attributes of an AD Host** action to update a specific directory property on computer accounts in the case, such as updating a computer's `Description` field with incident notes. The action automatically identifies the target computers from the case and applies the new value.

This action runs on the Google SecOps `Hostname` entity.

#### Action inputs

The **Update attributes of an AD Host** action requires the following parameters:

Parameter | Description  
---|---  
`Attribute Name` | Required. The name of the attribute to update, such as `Description`.  
`Attribute Value` | Required. The new value for the attribute.  
  
#### Action outputs

The **Update attributes of an AD Host** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Update attributes of an AD Host** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated attribute "ATTRIBUTE_NAME" on the following hosts in Active Directory: ENTITY_ID_LIST` | The action succeeded.  
`Action wasn't able to update attribute "ATTRIBUTE_NAME" on the following hosts in Active Directory: ENTITY_ID_LIST` | The action failed for the specified hosts.Verify that the service account has write permission for the specified attribute on the target computer accounts and that the value format is valid for that attribute.  
`The following hosts were not found in Active Directory: ENTITY_ID_LIST` | The action failed for the specified hosts.Verify that the computer accounts exist in Active Directory and match the `Hostname` entities in the case.  
`No hosts were updated in Active Directory.` | The action failed.Confirm that the case contains valid `Hostname` entities and that the service account has permission to update the specified attribute.  
`Error executing action "Update attributes of an AD Host". Reason: Provided attribute doesn't exist in Active Directory.` | The action failed.Check the spelling of the attribute in the `Attribute Name` parameter and confirm that it is a valid Active Directory computer attribute.  
`Error executing action "Update attributes of an AD Host". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, input parameters, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update attributes of an AD Host** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Update attributes of an AD User

Use the **Update attributes of an AD User** action to update a specific directory property on user accounts in the case, such as updating a user's `Description`, `title`, or `department` field. The action automatically identifies the target users from the case and applies the new value.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Update attributes of an AD User** action requires the following parameters:

Parameter | Description  
---|---  
`Attribute Name` | Required. The name of the attribute to update, such as `Description`.  
`Attribute Value` | Required. The new value for the attribute.  
  
#### Action outputs

The **Update attributes of an AD User** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Update attributes of an AD User** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated attribute "ATTRIBUTE_NAME" for the following users in Active Directory: ENTITY_ID_LIST` | The action succeeded.  
`Action wasn't able to update attribute "ATTRIBUTE_NAME" for the following users in Active Directory: ENTITY_ID_LIST` | The action failed for the specified users.Verify that the service account has write permission for the specified attribute on the target user accounts and that the value format is valid for that attribute.  
`The following users were not found in Active Directory: ENTITY_ID_LIST` | The action failed for the specified users.Verify that the user accounts exist in Active Directory and match the `User` entities in the case.  
`No users were updated in Active Directory.` | The action failed.Confirm that the case contains valid `User` entities and that the service account has permission to update the specified attribute.  
`Error executing action "Update attributes of an AD User". Reason: Provided attribute doesn't exist in Active Directory.` | The action failed.Check the spelling of the attribute in the `Attribute Name` parameter and confirm that it is a valid Active Directory user attribute.  
`Error executing action "Update attributes of an AD User". Reason: ERROR_REASON` | The action failed.Check the connection to the Active Directory server, input parameters, or service account credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update attributes of an AD User** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
