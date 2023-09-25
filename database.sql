create table regions
(
    id       uuid not nullprimary key,
    name     text unique,
    endpoint text
);

alter table regions
    owner to postgres;

create table zones
(
    id        uuid not null primary key,
    name      text unique,
    region_id uuid references regions
);

alter table zones
    owner to postgres;

create table records
(
    id      uuid not null
        primary key,
    name    text,
    type    text,
    value   text,
    zone_id uuid references zones,
    unique (name, value, type, zone_id)
);

alter table records owner to postgres;

INSERT INTO public.zones (id, name, region_id) VALUES ('bad2103a-e4ce-4766-bf02-77a0eec3b2ec', 'test.com', 'bb1d396f-30ee-4320-8667-82b651d6ac49');
INSERT INTO public.zones (id, name, region_id) VALUES ('2dba5a28-dfd6-4219-b2ed-b316862ca574', 'test.fr', '51a59577-4063-4dc1-b12a-4927fe6589d8');
INSERT INTO public.regions (id, name, endpoint) VALUES ('51a59577-4063-4dc1-b12a-4927fe6589d8', 'paris-2', 'http://172.20.0.4:8080/');
INSERT INTO public.regions (id, name, endpoint) VALUES ('bb1d396f-30ee-4320-8667-82b651d6ac49', 'paris-1', 'http://172.20.0.3:8080/');

