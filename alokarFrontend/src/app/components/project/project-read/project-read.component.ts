import { Component, OnInit } from '@angular/core';
import { Project } from '../project.model';
import { ProjectService } from '../project.service';

@Component({
    selector: 'app-project-read',
    templateUrl: './project-read.component.html',
    styleUrls: ['./project-read.component.css']
})
export class ProjectReadComponent implements OnInit {

    projects: Project[]
    totalRecords: any;
    page: number = 1

    constructor(private projectService: ProjectService) { }

    ngOnInit(): void {
        this.getProjects();
    }

    getProjects() {
        this.projectService.read().subscribe(projects => {
            this.projects = projects;
            this.totalRecords = projects.length;
        })
    }

    // details(id) {
    //     this.projectService.readByPk(this.projects).subscribe(projects => {
    //         this.projects = projects;
    //     })
    // }

}
