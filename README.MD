# Python and React: Education Application Example

### Github repo: Sigma-EducationApp
## Introduction
 This repo is a Python 3.7 on the server side and React on the frontend application that demonstrates:

* Authentication with DocuSign via the
[JSON Web Token (JWT) Grant](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-jsonwebtoken).

1. **Reguest Minor/Major Change.**
   [Source.](./app/api/requests.py)
   This example sends an envelope based on HTML template with filled-in user data and then initiate embedded signing ceremony for single signer.
   The DocuSign signing ceremony is initiated from your website.
   Anchor text ([AutoPlace](https://support.docusign.com/en/guides/AutoPlace-New-DocuSign-Experience)) is used to position the signing fields in the documents.
1. **View an Unofficial Transcript.**
   [Source.](./app/api/clickwrap.py)
   This example demonstates usage of Click API.
   So right after form submission confirmation popup received from DocuSign API appears. 
   And only after it's confirmation user is able to download an unofficial transcript.
   [More information about ClickAPI](https://developers.docusign.com/click-api) 
1. **Register for Extra-Curricular Activity.**
   [Source.](./app/api/requests.py)
   This example demonstrate how to use Envelopes combined with Payment Gateways.
   Example send an envelope based on HTML template and in addition add payment feature to the document.
   So after signing user will be able to pay for signed feature. 
   To use this example, create a test payments gateway for your developer sandbox account.

## Installation

### Prerequisites
1. A DocuSign Developer Sandbox account (email and password) on [demo.docusign.net](https://demo.docusign.net).
   Create a [free account](https://go.docusign.com/sandbox/productshot/?elqCampaignId=16535).
1. A DocuSign Integration Key (a client ID) that is configured to use the
   JSON Web Token (JWT) Grant.
   You will need the **Integration Key** itself, and its **RSA Keypair**.
   
   To use application you have to add DNS name of the server **Redirect URI** to your Integration key.
   
   This [**video**](https://www.youtube.com/watch)
   demonstrates how to create an Integration Key (client id) for a
   user application like this example. 

1. Python 3.7.
1. [venv](https://docs.python.org/3/library/venv.html#module-venv).
1. [Node.js](https://nodejs.org/) v10+.

### Required Environment Variables
**DS_CLIENT_ID** - Integrator Key is the same as client id 
**DS_IMPERSONATED_USER_GUID** - API Account ID
**DS_TARGET_ACCOUNT_ID** - Target account id. Use FALSE to indicate that the user's default
**DS_PAYMENT_GATEWAY_ID** - Payment Gateway ID (Only Stripe method supported)
**DS_PAYMENT_GATEWAY_NAME** - Payment Gateway Name
**DS_PAYMENT_GATEWAY_DISPLAY_NAME** - Payment Gateway Display Name
**DS_PRIVATE_KEY** - Private key string - source or path, for instance: /app/id_rsa
**REACT_APP_DS_RETURN_URL** - URL where backend of the Application is located (if you run it locally - http://localhost:3000)
**REACT_APP_API_BASE_URL** - URL of the Frontend. Will be used by Docusign to redirect back after signing ceremony. (if you run it locally - http://localhost:5001/api)
**REACT_APP_DS_AUTH_SERVER** - The DS Authentication server (for testing purposes use - https://account-d.docusign.com)
**REACT_APP_DS_DEMO_SERVER** - Link to Demo Docusing Server (for testing purposes use - https://demo.docusign.net)
**REACT_APP_DS_CLICKWRAP_URL** - Link to the hosted Clickwrap Client (for testing purposes use - `//demo.docusign.net/clickapi/sdk/latest/docusign-click.js`)

### Installation steps
**Manually**
1. Download or clone this repository to your workstation to directory **Sigma-InsuranceApp**
1. **`cd Sigma-InsuranceApp`** directory
1. Install python packages **`pip install -r requirements.txt`**
1. Install react dependencies using [npm](https://www.npmjs.com/) package manager  **npm install**
1. Update the **.env** file with the Integration Key and other settings.

   **Note:** Protect your Integration Key and secret--you
   should ensure that **.env** file will not be stored in your source code
   repository.

**Using installation scripts**
1. Download or clone this repository to your workstation to directory **Sigma-InsuranceApp**
1. **`cd Sigma-InsuranceApp/scripts`**
1. **`./install.sh`**
1. Update the **.env** file with the Integration Key and other settings.

   **Note:** Protect your Integration Key and secret--you
   should ensure that **.env** file will not be stored in your source code
   repository.
   
### Running
**Manually**
1. **`cd Sigma-InsuranceApp`**
1. **`flask run --port 5001`**
1. **`npm start`**
1. Open a browser to **http://localhost:3000**

**Using installation scripts**
All installation scripts located in **scripts** folder.
1. **`cd scripts`**
1. **`./run.sh`**
1. Open a browser to **http://localhost:3000**

### Additional instalation scripts
All installation scripts located in **scripts** folder.
1. To stop application run **`./stop.sh`**
1. To remove virtual environment and modules run **`./clean.sh`**

# Configuring a DocuSign payments gateway

DocuSign offers built-in connections to multiple payment
gateways. The payments example uses a demo account via the Stripe
gateway service.

## Creating the payments gateway account

1. Login to demo.docusign.net and go to the Admin Panel.
1. On the Integrations / Payments screen, click Stripe.
1. For development, you can skip the Stripe account application
   by using the `Skip this account form` on the top of the page.
1. Next, the Admin Panel will show that an enabled Stripe
   payment gateway account has been associated with your
   DocuSign demo sandbox account.
1. Configure the example launcher with the gateway account id shown in the Admin Panel.
1. [Credit card numbers for testing](https://stripe.com/docs/testing)

## Additional documentation
See the 
[Managing Payment Gateways](https://support.docusign.com/en/guides/managing-payment-gateways)
documentation. 

Then add the payment gateway account id to the **.env** file.

## License and additional information

### License
This repository uses the MIT License. See the [LICENSE](./LICENSE) file for more information.

### Additional Resources
* [DocuSign Developer Center](https://developers.docusign.com)
* [DocuSign API on Twitter](https://twitter.com/docusignapi)
* [DocuSign For Developers on LinkedIn](https://www.linkedin.com/showcase/docusign-for-developers/)
* [DocuSign For Developers on YouTube](https://www.youtube.com/channel/UCJSJ2kMs_qeQotmw4-lX2NQ)

