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
def accessing_data(request: Request):
    vm = ViewModelBase(request, "Accessing Data")
    return vm.to_dict()


@router.get('/resources/add-citation')
@template("resources/add-citation.html")
def add_citation(request: Request):
    vm = ViewModelBase(request, "Add Citation")
    return vm.to_dict()


@router.get('/resources/assessing-fitness-for-use')
@template("resources/assessing-fitness-for-use.html")
def assessing_fitness_for_use(request: Request):
    vm = ViewModelBase(request, "Assessing Fitness for Use")
    return vm.to_dict()


@router.get('/resources/citing-data')
@template("resources/citing-data.html")
def citing_data(request: Request):
    vm = ViewModelBase(request, "Citing Data")
    return vm.to_dict()


@router.get('/resources/cleaning-data-and-quality-control')
@template("resources/cleaning-data-and-quality-control.html")
def cleaning_data_and_quality_control(request: Request):
    vm = ViewModelBase(request, "Cleaning Data and Quality Control")
    return vm.to_dict()


@router.get('/resources/create-a-data-catalog')
@template("resources/create-a-data-catalog.html")
def create_a_data_catalog(request: Request):
    vm = ViewModelBase(request, "Create a Data Catalog")
    return vm.to_dict()


@router.get('/resources/creating-metadata-during-the-research-lifecycle')
@template("resources/creating-metadata-during-the-research-lifecycle.html")
def creating_metadata_during_the_research_lifecycle(request: Request):
    vm = ViewModelBase(request, "Creating Metadata During the Research Lifecycle")
    return vm.to_dict()


@router.get('/resources/creating-metadata-for-publication')
@template("resources/creating-metadata-for-publication.html")
def creating_metadata_for_publication(request: Request):
    vm = ViewModelBase(request, "Creating Metadata for Publication")
    return vm.to_dict()


@router.get('/resources/data-exploration')
@template("resources/data-exploration.html")
def data_exploration(request: Request):
    vm = ViewModelBase(request, "Data Exploration")
    return vm.to_dict()


@router.get('/resources/data-management-planning')
@template("resources/data-management-planning.html")
def data_management_planning(request: Request):
    vm = ViewModelBase(request, "Data Management Planning")
    return vm.to_dict()


@router.get('/resources/data-package-pages')
@template("resources/data-package-pages.html")
def data_package_pages(request: Request):
    vm = ViewModelBase(request, "Data Package Pages")
    return vm.to_dict()


@router.get('/resources/deprecating-a-data-package')
@template("resources/deprecating-a-data-package.html")
def deprecating_a_data_package(request: Request):
    vm = ViewModelBase(request, "Deprecating a Data Package")
    return vm.to_dict()


@router.get('/resources/designing-a-data-package')
@template("resources/designing-a-data-package.html")
def designing_a_data_package(request: Request):
    vm = ViewModelBase(request, "Designing a Data Package")
    return vm.to_dict()


@router.get('/resources/evaluating-a-data-package')
@template("resources/evaluating-a-data-package.html")
def evaluating_a_data_package(request: Request):
    vm = ViewModelBase(request, "Evaluating a Data Package")
    return vm.to_dict()


@router.get('/resources/event-notifications')
@template("resources/event-notifications.html")
def event_notifications(request: Request):
    vm = ViewModelBase(request, "Event Notifications")
    return vm.to_dict()


@router.get('/resources/featured-data')
@template("resources/featured-data.html")
def featured_data(request: Request):
    vm = ViewModelBase(request, "Featured Data")
    return vm.to_dict()


@router.get('/resources/finding-data')
@template("resources/finding-data.html")
def finding_data(request: Request):
    vm = ViewModelBase(request, "Finding Data")
    return vm.to_dict()


@router.get('/resources/information-manager-quickstart')
@template("resources/information-manager-quickstart.html")
def information_manager_quickstart(request: Request):
    vm = ViewModelBase(request, "Information Manager Quickstart")
    return vm.to_dict()


@router.get('/resources/licensing-data')
@template("resources/licensing-data.html")
def licensing_data(request: Request):
    vm = ViewModelBase(request, "Licensing Data")
    return vm.to_dict()


@router.get('/resources/orcid-id')
@template("resources/orcid-id.html")
def orcid_id(request: Request):
    vm = ViewModelBase(request, "ORCID Id")
    return vm.to_dict()


@router.get('/resources/provenance-metadata')
@template("resources/provenance-metadata.html")
def provenance_metadata(request: Request):
    vm = ViewModelBase(request, "Provenance Metadata")
    return vm.to_dict()


@router.get('/resources/publishing-a-data-package')
@template("resources/publishing-a-data-package.html")
def publishing_a_data_package(request: Request):
    vm = ViewModelBase(request, "Publishing a Data Package")
    return vm.to_dict()


@router.get('/resources/quality-assurance')
@template("resources/quality-assurance.html")
def quality_assurance(request: Request):
    vm = ViewModelBase(request, "Quality Assurance")
    return vm.to_dict()


@router.get('/resources/reporting-to-funders')
@template("resources/reporting-to-funders.html")
def reporting_to_funders(request: Request):
    vm = ViewModelBase(request, "Reporting to Funders")
    return vm.to_dict()


@router.get('/resources/repository-environments')
@template("resources/repository-environments.html")
def repository_environments(request: Request):
    vm = ViewModelBase(request, "Repository Environments")
    return vm.to_dict()


@router.get('/resources/resources-for-data-authors')
@template("resources/resources-for-data-authors.html")
def resources_for_data_authors(request: Request):
    vm = ViewModelBase(request, "Resources for Data Authors")
    return vm.to_dict()


@router.get('/resources/resources-for-data-users')
@template("resources/resources-for-data-users.html")
def resources_for_data_users(request: Request):
    vm = ViewModelBase(request, "Resources for Data Users")
    return vm.to_dict()


@router.get('/resources/resources-for-information-managers')
@template("resources/resources-for-information-managers.html")
def resources_for_information_managers(request: Request):
    vm = ViewModelBase(request, "Resources for Information Managers")
    return vm.to_dict()


@router.get('/resources/rest-api')
@template("resources/rest-api.html")
def rest_api(request: Request):
    vm = ViewModelBase(request, "REST API")
    return vm.to_dict()


@router.get('/resources/services')
@template("resources/services.html")
def services(request: Request):
    vm = ViewModelBase(request, "Services")
    return vm.to_dict()


@router.get('/resources/the-data-package')
@template("resources/the-data-package.html")
def the_data_package(request: Request):
    vm = ViewModelBase(request, "The Data Package")
    return vm.to_dict()


@router.get('/resources/the-edi-dashboard')
@template("resources/the-edi-dashboard.html")
def thea_edi_dashboard(request: Request):
    vm = ViewModelBase(request, "The EDI Dashboard")
    return vm.to_dict()


@router.get('/resources/thematic-standardization')
@template("resources/thematic-standardization.html")
def thematic_standardization(request: Request):
    vm = ViewModelBase(request, "Thematic Standardization")
    return vm.to_dict()


@router.get('/resources/the-review-process')
@template("resources/the-review-process.html")
def the_review_process(request: Request):
    vm = ViewModelBase(request, "The Review Process")
    return vm.to_dict()


@router.get('/resources/tracking-data-package-use')
@template("resources/tracking-data-package-use.html")
def tracking_data_package_use(request: Request):
    vm = ViewModelBase(request, "Tracking Data Package Use")
    return vm.to_dict()


@router.get('/resources/types-of-contributions')
@template("resources/types-of-contributions.html")
def types_of_contributions(request: Request):
    vm = ViewModelBase(request, "Types of Contributions")
    return vm.to_dict()


@router.get('/resources/updating-a-data-package')
@template("resources/updating-a-data-package.html")
def updating_a_data_package(request: Request):
    vm = ViewModelBase(request, "Updating a Data Package")
    return vm.to_dict()


@router.get('/resources/uploading-with-static-data-links')
@template("resources/uploading-with-static-data-links.html")
def uploading_with_static_data_links(request: Request):
    vm = ViewModelBase(request, "Uploading with Static Data Links")
    return vm.to_dict()


@router.get('/resources/why-publish-data')
@template("resources/why-publish-data.html")
def why_publish_data(request: Request):
    vm = ViewModelBase(request, "Why Publish Data")
    return vm.to_dict()

@router.get('/resources/adding-physical-metadata')
@template("resources/adding-physical-metadata.html")
def adding_physical_metadata(request: Request):
    vm = ViewModelBase(request, "Adding Physical Metadata")
    return vm.to_dict()
