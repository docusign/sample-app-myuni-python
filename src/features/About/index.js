import React from "react";
import { useTranslation } from "react-i18next";
import parse from "html-react-parser";

export const About = () => {
  const { t } = useTranslation("About");
  return (
    <div className="container">
      <br></br>

      <h2 id="sample-app">{t("Title")}</h2>
      <blockquote>{parse(t("Description"))}</blockquote>
      <p>
        <strong>
          {t("SourceButton")}
          <a
            target="_blank"
            href="https://github.com/docusign/sample-app-myuni-python"
            rel="noopener noreferrer"
          >
            {t("GitHubLink")}
          </a>
        </strong>
      </p>
      <br></br>
      <div className="row">
        <div className="col-md-6">
          {parse(t("Features"))}
        </div>
        <div className="col-md-6">
          <h3>{t("ToolsandLinks")}</h3>
          <p><strong>{t("DeveloperCenter")}</strong><br></br>
            <a
              target="_blank"
              href="https://developers.docusign.com"
              rel="noopener noreferrer"
            >
              {t("DeveloperCenterLink")}
            </a>
          </p>
          <p><strong>{t("APICodeExamples")}</strong><br></br>
            <a
              target="_blank"
              href="https://developers.docusign.com/esign-rest-api/code-examples"
              rel="noopener noreferrer"
            >
              {t("APICodeExamplesLink")}
            </a>
          </p>
          <p><strong>{t("ESignatureDocumentation")}</strong><br></br>
            <a
              target="_blank"
              href="https://developers.docusign.com/esign-rest-api/reference"
              rel="noopener noreferrer"
            >
              {t("ESignatureDocumentationLink")}
            </a>
          </p>
          <p><strong>{t("DeveloperCommunity")}</strong><br></br>
            <a
              target="_blank"
              href="http://stackoverflow.com/questions/tagged/docusignapi"
              rel="noopener noreferrer"
            >
              {t("DeveloperCommunityLink")}
            </a>
          </p>
        </div>
      </div>
      {parse(t("AboutDocuSign"))}

      <br></br>

      <p>
        <a href="http://www.docusign.com/"> {t("DocuSignLink")}</a>
      </p>
    </div>
  );
};
