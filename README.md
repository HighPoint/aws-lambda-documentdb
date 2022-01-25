# aws-lambda-documentdb

A simple AWS Lambda connection to DocumentDB.

The rds-combined-ca-bundle.pem should be placed in the same folder as the lambda_handler.py.

DocumentDB is created in a VPC. The Lambda should be in the same VPC or have IAM priviledges for AmazonVPCFullAccess.
