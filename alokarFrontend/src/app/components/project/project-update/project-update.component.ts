import { identifierModuleUrl } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Project } from '../project.model';
import { ProjectService } from '../project.service';

@Component({
    selector: 'app-project-update',
    templateUrl: './project-update.component.html',
    styleUrls: ['./project-update.component.css']
})
export class ProjectUpdateComponent implements OnInit {

    project: Project

    constructor(private projectService: ProjectService, private router: ActivatedRoute, private route: Router) { }

    ngOnInit(): void {
        const id = this.router.snapshot.paramMap.get('id');
        this.projectService.readByPk(id).subscribe(project => {
            this.project = project;
        })
    }

    updateProject(): void {
        const id = this.router.snapshot.paramMap.get('id');
        this.projectService.update(this.project, id).subscribe(() => {
            this.projectService.showMessage('Projeto editado com sucesso.');
            this.route.navigate([`/projects/`]);
        })
    }

}
