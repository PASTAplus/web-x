#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: about

:Synopsis:

:Author:
    servilla

:Created:
    6/3/21
"""
import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get('/resources/accessing-data')
@template("resources/accessing-data.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Accessing Data")
    return vm.to_dict()


@router.get('/resources/add-citation')
@template("resources/add-citation.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Add Citation")
    return vm.to_dict()


@router.get('/resources/assessing-fitness-for-use')
@template("resources/assessing-fitness-for-use.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Assessing Fitness for Use")
    return vm.to_dict()


@router.get('/resources/citing-data')
@template("resources/citing-data.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Citing Data")
    return vm.to_dict()


@router.get('/resources/cleaning-data-and-quality-control')
@template("resources/cleaning-data-and-quality-control.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Cleaning Data and Quality Control")
    return vm.to_dict()


@router.get('/resources/create-a-data-catalog')
@template("resources/create-a-data-catalog.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Create a Data Catalog")
    return vm.to_dict()


@router.get('/resources/creating-metadata-during-the-research-lifecycle')
@template("resources/creating-metadata-during-the-research-lifecycle.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Creating Metadata During the Research Lifecycle")
    return vm.to_dict()


@router.get('/resources/creating-metadata-for-publication')
@template("resources/creating-metadata-for-publication.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Creating Metadata for Publication")
    return vm.to_dict()


@router.get('/resources/data-exploration')
@template("resources/data-exploration.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Data Exploration")
    return vm.to_dict()


@router.get('/resources/data-management-planning')
@template("resources/data-management-planning.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Data Management Planning")
    return vm.to_dict()


@router.get('/resources/data-package-pages')
@template("resources/data-package-pages.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Data Package Pages")
    return vm.to_dict()


@router.get('/resources/designing-a-data-package')
@template("resources/designing-a-data-package.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Designing a Data Package")
    return vm.to_dict()


@router.get('/resources/evaluating-a-data-package')
@template("resources/evaluating-a-data-package.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Evaluating a Data Package")
    return vm.to_dict()


@router.get('/resources/event-notifications')
@template("resources/event-notifications.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Event Notifications")
    return vm.to_dict()


@router.get('/resources/featured-data')
@template("resources/featured-data.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Featured Data")
    return vm.to_dict()


@router.get('/resources/finding-data')
@template("resources/finding-data.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Finding Data")
    return vm.to_dict()


@router.get('/resources/information-manager-quickstart')
@template("resources/information-manager-quickstart.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Information Manager Quickstart")
    return vm.to_dict()


@router.get('/resources/licensing-data')
@template("resources/licensing-data.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Licensing Data")
    return vm.to_dict()


@router.get('/resources/orcid-id')
@template("resources/orcid-id.html")
def authors(request: Request):
    vm = ViewModelBase(request, "ORCID Id")
    return vm.to_dict()


@router.get('/resources/provenance-metadata')
@template("resources/provenance-metadata.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Provenance Metadata")
    return vm.to_dict()


@router.get('/resources/publishing-a-data-package')
@template("resources/publishing-a-data-package.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Publishing a Data Package")
    return vm.to_dict()


@router.get('/resources/quality-assurance')
@template("resources/quality-assurance.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Quality Assurance")
    return vm.to_dict()


@router.get('/resources/reporting-to-funders')
@template("resources/reporting-to-funders.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Reporting to Funders")
    return vm.to_dict()


@router.get('/resources/repository-environments')
@template("resources/repository-environments.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Repository Environments")
    return vm.to_dict()


@router.get('/resources/resources-for-data-authors')
@template("resources/resources-for-data-authors.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Resources for Data Authors")
    return vm.to_dict()


@router.get('/resources/resources-for-data-users')
@template("resources/resources-for-data-users.html")
def users(request: Request):
    vm = ViewModelBase(request, "Resources for Data Users")
    return vm.to_dict()


@router.get('/resources/resources-for-information-managers')
@template("resources/resources-for-information-managers.html")
def managers(request: Request):
    vm = ViewModelBase(request, "Resources for Information Managers")
    return vm.to_dict()


@router.get('/resources/rest-api')
@template("resources/rest-api.html")
def authors(request: Request):
    vm = ViewModelBase(request, "REST API")
    return vm.to_dict()


@router.get('/resources/services')
@template("resources/services.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Services")
    return vm.to_dict()


@router.get('/resources/the-data-package')
@template("resources/the-data-package.html")
def authors(request: Request):
    vm = ViewModelBase(request, "The Data Package")
    return vm.to_dict()


@router.get('/resources/the-edi-dashboard')
@template("resources/the-edi-dashboard.html")
def authors(request: Request):
    vm = ViewModelBase(request, "The EDI Dashboard")
    return vm.to_dict()


@router.get('/resources/thematic-standardization')
@template("resources/thematic-standardization.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Thematic Standardization")
    return vm.to_dict()


@router.get('/resources/the-review-process')
@template("resources/the-review-process.html")
def authors(request: Request):
    vm = ViewModelBase(request, "The Review Process")
    return vm.to_dict()


@router.get('/resources/tracking-data-package-use')
@template("resources/tracking-data-package-use.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Tracking Data Package Use")
    return vm.to_dict()


@router.get('/resources/types-of-contributions')
@template("resources/types-of-contributions.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Types of Contributions")
    return vm.to_dict()


@router.get('/resources/updating-a-data-package')
@template("resources/updating-a-data-package.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Updating a Data Package")
    return vm.to_dict()


@router.get('/resources/uploading-with-static-data-links')
@template("resources/uploading-with-static-data-links.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Uploading with Static Data Links")
    return vm.to_dict()


@router.get('/resources/why-publish-data')
@template("resources/why-publish-data.html")
def authors(request: Request):
    vm = ViewModelBase(request, "Why Publish Data")
    return vm.to_dict()
