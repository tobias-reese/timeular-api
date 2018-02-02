#!/bin/bash
java -jar ../swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i http://developers.timeular.com/public-api/swagger/public-api.v2.yaml -l python -DpackageName=timular_api --git-user-id tobias-reese --git-repo-id timular-api -o .
