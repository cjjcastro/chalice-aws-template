# Chalice AWS Application Template

This repository contains a basic template to kickstart the development of a serverless application using Chalice AWS.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- Python (version 3.6 or higher)
- AWS CLI
- AWS account with permissions to create resources such as AWS Lambda, API Gateway, etc.

## Configuration

1. Clone this repository to your local machine: `git clone https://github.com/cjjcastro/chalice-aws-template.git`
2. Navigate to the project directory: `cd template-chalice-aws`
3. Install project dependencies: `pip install -r requirements.txt`
4. Configure your AWS credentials using the `aws configure` command or by setting the environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
5. Customize the application according to your needs by modifying the `app.py` file and adding new endpoints as needed.

## Usage

To run the application locally, execute the following command:

```bash
chalice local
```

This will start a local server on the default port (8000 by default).

To deploy the application to AWS, run the following command:

```bash
chalice deploy
```

This will deploy the application to your AWS account and provide a URL to access the API endpoints.

## Contributing

If you wish to contribute improvements or fixes, please open an issue or submit a pull request. I'll be happy to review and merge your contributions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
