# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 13:13
from __future__ import unicode_literals

import re
import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import WEIPDCRM.models.section
import WEIPDCRM.models.setting
import WEIPDCRM.models.version


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('preferences', '0002_auto_20170110_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255, verbose_name='Name')),
                ('created_at', models.DateTimeField(verbose_name='Created At')),
                ('c_package', models.CharField(max_length=255, verbose_name='Package')),
                ('c_version', models.CharField(max_length=255, verbose_name='Version')),
                ('online_icon', models.ImageField(blank=True, max_length=255, upload_to=b'', verbose_name='Online Icon')),
            ],
            options={
                'verbose_name': 'Package',
                'db_table': 'package_view',
                'managed': False,
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('job_id', models.CharField(default=None, max_length=64, null=True, verbose_name='Job ID')),
                ('details', models.TextField(blank=True, default='', help_text='Tell others what did you do this time before you rebuild the repository.', null=True, verbose_name='Details')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Build',
                'verbose_name_plural': 'Builds',
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('descriptor', models.CharField(help_text='Example: iPhone 7 Plus', max_length=255, verbose_name='Descriptor')),
                ('subtype', models.CharField(help_text='Example: iPhone9,2', max_length=255, verbose_name='Subtype')),
                ('platform', models.CharField(blank=True, help_text='Example: A1661/A1784/A1785', max_length=255, verbose_name='Platform')),
                ('icon', models.FileField(blank=True, help_text='Choose an Icon (*.png) to upload', max_length=255, null=True, upload_to='device-icons', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Device Type',
                'verbose_name_plural': 'Device Types',
            },
        ),
        migrations.CreateModel(
            name='OSVersion',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('descriptor', models.CharField(help_text='Example: 10.2', max_length=255, verbose_name='Version')),
                ('build', models.CharField(help_text='Example: 14C92/11A466', max_length=255, verbose_name='Build')),
                ('icon', models.FileField(blank=True, help_text='Choose an Icon (*.png) to upload', max_length=255, null=True, upload_to='os-icons', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'iOS Version',
                'verbose_name_plural': 'iOS Versions',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('origin', models.CharField(default='', help_text='This is used by Cydia as the name of the repository as shown in the source editor (and elsewhere). This should be a longer, but not insanely long, description of the repository.', max_length=255, verbose_name='Origin')),
                ('label', models.CharField(default='', help_text="On the package list screens, Cydia shows what repository and section packages came from. This location doesn't have much room, though, so this field should contain a shorter/simpler version of the name of the repository that can be used as a tag.", max_length=255, verbose_name='Label')),
                ('suite', models.CharField(blank=True, default='stable', help_text='Just set this to "stable". This field might not be required, but who really knows? I, for certain, do not.', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')], verbose_name='Suite')),
                ('version', models.CharField(default='0.0.1-1', help_text='This is an arbitrary version number that nothing actually parses. I am going to look into seeing how required it is.', max_length=255, verbose_name='Version')),
                ('codename', models.CharField(blank=True, default='', help_text='In an "automatic" repository you might store multiple distributions of software for different target systems. For example: apt.saurik.com\'s main repository houses content both for desktop Debian Etch systems as well as the iPhone. This codename then describes what distribution we are currently looking for.', max_length=255, verbose_name='Codename')),
                ('architectures', models.CharField(blank=True, default='iphoneos-arm', help_text='To verify a repository is for the specific device you are working with APT looks in the release file for this list. You must specify all of the architectures that appear in your Packages file here. Again, we use darwin-arm for 1.1.x and iphoneos-arm for 2.x.', max_length=255, verbose_name='Architectures')),
                ('components', models.CharField(blank=True, default='main', help_text='Just set this to "main". This field might not be required, but who really knows? I, for certain, do not.', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')], verbose_name='Components')),
                ('description', models.TextField(blank=True, help_text='On the package source screen a short description is listed of the repository. This description may eventually work similarly to that of a package (with a long/short variety and the aforementioned encoding), but for right now only the shorter description is displayed directly on the list.', verbose_name='Description')),
                ('keywords', models.CharField(blank=True, default='', help_text='Separated by commas.', max_length=255, verbose_name='Keywords')),
                ('icon', models.FileField(blank=True, help_text='Choose an Icon (*.png) to upload', max_length=255, null=True, upload_to='repository-icons', verbose_name='Repository Icon')),
                ('support', models.URLField(blank=True, help_text='Official site to provide support.', max_length=255, null=True, verbose_name='Support')),
                ('email', models.EmailField(blank=True, help_text="Maintainer's E-mail to provide support.", max_length=255, null=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Release',
                'verbose_name_plural': 'Releases',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('name', models.CharField(help_text='This is a general field that gives the package a category based on the software that it installs. You will not be able to edit its name after assigning any package under it.', max_length=255, unique=True, validators=[WEIPDCRM.models.section.validator_underscore], verbose_name='Name')),
                ('icon', models.FileField(blank=True, help_text='Choose an Icon (*.png) to upload', max_length=255, null=True, upload_to='section-icons', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('preferences_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='preferences.Preferences')),
                ('packages_compression', models.IntegerField(choices=[(0, 'Plain'), (1, 'Gzip'), (2, 'Plain and Gzip'), (3, 'Bzip'), (4, 'Plain and Bzip'), (5, 'Gzip and Bzip'), (6, 'All (Recommended)')], default=6, help_text='Please change the compression method if error occurred when try to rebuild the list.', verbose_name='Packages Compression')),
                ('packages_validation', models.IntegerField(choices=[(0, 'No validation'), (1, 'MD5Sum'), (2, 'MD5Sum & SHA1'), (3, 'MD5Sum & SHA1 & SHA256 (Recommended)'), (4, 'MD5Sum & SHA1 & SHA256 & SHA512')], default=3, help_text='You need to update hashes manually.', verbose_name='Packages Validation')),
                ('downgrade_support', models.BooleanField(default=True, help_text='Allow multiple versions to exist in the latest package list.', verbose_name='Downgrade Support')),
                ('advanced_mode', models.BooleanField(default=False, help_text='Check it to generate awesome depiction page for each version.', verbose_name='Auto Depiction')),
                ('atomic_storage', models.BooleanField(default=False, help_text='Generate a new copy of package after editing control columns.', verbose_name='Atomic Storage')),
                ('resources_alias', models.CharField(default='/resources/', help_text='You can specify alias for resources path in Nginx or other HTTP servers, which is also necessary for CDN speedup.', max_length=255, validators=[WEIPDCRM.models.setting.validator_basic, WEIPDCRM.models.setting.validate_alias], verbose_name='Resources Alias')),
                ('enable_pdiffs', models.BooleanField(default=False, help_text='If package list is extremely large, you should enable this to allow incremental update.', validators=[WEIPDCRM.models.setting.validate_pdiffs], verbose_name='Enable pdiffs')),
                ('rest_api', models.BooleanField(default=False, help_text='Upload packages using HTTP, manage your repositories, snapshots, published repositories etc.', validators=[WEIPDCRM.models.setting.validate_rest_api], verbose_name='Enable Rest API')),
                ('gpg_signature', models.BooleanField(default=False, help_text="Verify the integrity of the repository. Run 'gpg --gen-key' before you enable this feature.", validators=[WEIPDCRM.models.setting.validate_gpg], verbose_name='Enable GPG Signature')),
                ('web_server', models.IntegerField(choices=[(0, 'Nginx'), (1, 'Apache'), (2, 'Tomcat')], default=0, help_text='This will help DCRM redirect download request properly.', validators=[WEIPDCRM.models.setting.validate_web_server], verbose_name='Web Server')),
                ('redirect_resources', models.IntegerField(choices=[(0, 'None'), (1, 'Moved'), (2, 'Accel')], default=0, help_text='None - Read resources and return.<br />Moved - Return 301/302 responses and redirect to the real resource urls.<br />Accel - Redirect resource requests to WEB servers without changing urls.', verbose_name='Redirect Methods')),
                ('download_count', models.BooleanField(default=False, help_text='Count every download. You should configure Nginx or other Web servers before you enable this feature.', verbose_name='Download Count')),
                ('download_cydia_only', models.BooleanField(default=False, help_text='Protect downloading from any other tools except Cydia. You should configure Nginx or other Web servers before you enable this feature.', verbose_name='Cydia Only')),
                ('comments', models.BooleanField(default=False, help_text='Enable comments', verbose_name='Comments')),
                ('active_release', models.ForeignKey(blank=True, default=None, help_text='Each repository should have an active release, otherwise it will not be recognized by any advanced package tools.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='WEIPDCRM.Release', verbose_name='Active Release')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
            bases=('preferences.preferences',),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(db_index=True, default=False, verbose_name='Enabled')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('update_logs', models.TextField(blank=True, default='', verbose_name='Update Logs')),
                ('storage', models.FileField(max_length=255, upload_to='debs', verbose_name='Storage')),
                ('online_icon', models.FileField(blank=True, help_text='Choose an Icon (*.png) to upload', max_length=255, null=True, upload_to='package-icons', verbose_name='Online Icon')),
                ('c_icon', models.CharField(blank=True, default=None, help_text='If there is no "Online Icon", this field will be taken.', max_length=255, null=True, verbose_name='Icon')),
                ('c_md5', models.CharField(default='', max_length=32, verbose_name='MD5Sum')),
                ('c_sha1', models.CharField(default='', max_length=40, verbose_name='SHA1')),
                ('c_sha256', models.CharField(default='', max_length=64, verbose_name='SHA256')),
                ('c_sha512', models.CharField(default='', max_length=128, verbose_name='SHA512')),
                ('c_size', models.BigIntegerField(default=0, help_text='The exact size of the package, in bytes.', verbose_name='Size')),
                ('download_times', models.IntegerField(default=0, verbose_name='Download Times')),
                ('c_installed_size', models.BigIntegerField(blank=True, default=0, help_text="The approximate total size of the package's installed files, in KiB units.", null=True, verbose_name='Installed-Size')),
                ('c_package', models.CharField(db_index=True, help_text='This is the "identifier" of the package. This should be, entirely in lower case, a reversed hostname (much like a "bundleIdentifier" in Apple\'s Info.plist files).', max_length=255, validators=[WEIPDCRM.models.version.validate_reversed_domain], verbose_name='Package')),
                ('c_version', models.CharField(db_index=True, default='1.0-1', help_text="A package's version indicates two separate values: the version of the software in the package, and the version of the package itself. These version numbers are separated by a hyphen.", max_length=255, validators=[WEIPDCRM.models.version.validate_version], verbose_name='Version')),
                ('maintainer_name', models.CharField(blank=True, default='', help_text='It is typically the person who created the package, as opposed to the author of the software that was packaged.', max_length=255, null=True, validators=[WEIPDCRM.models.version.validate_name], verbose_name='Maintainer')),
                ('maintainer_email', models.EmailField(blank=True, default='', max_length=255, null=True, verbose_name='Maintainer Email')),
                ('c_description', models.TextField(blank=True, default='', help_text='The first line (after the colon) should contain a short description to be displayed on the package lists underneath the name of the package. Optionally, one can choose to replace that description with an arbitrarily long one that will be displayed on the package details screen.', null=True, verbose_name='Description')),
                ('rich_description', models.TextField(blank=True, default='', help_text='HTML Displayed on the auto depiction page (mobile).', null=True, verbose_name='Rich Description')),
                ('c_tag', models.TextField(blank=True, default='', help_text='List of tags describing the qualities of the package. The description and list of supported tags can be found in the debtags package.', null=True, verbose_name='Tag')),
                ('c_architecture', models.CharField(blank=True, default='', help_text='This describes what system a package is designed for, as .deb files are used on everything from the iPhone to your desktop computer. The correct value for iPhoneOS 1.0.x/1.1.x is "darwin-arm". If you are deploying to iPhoneOS 1.2/2.x you should use "iphoneos-arm".', max_length=255, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')], verbose_name='Architecture')),
                ('c_name', models.CharField(blank=True, default='Untitled Package', help_text='When the package is shown in Cydia\'s lists, it is convenient to have a prettier name. This field allows you to override this display with an arbitrary string. This field may change often, whereas the "Package" field is fixed for the lifetime of the package.', max_length=255, null=True, verbose_name='Name')),
                ('author_name', models.CharField(blank=True, default='', help_text='In contrast, the person who wrote the original software is called the "author". This name will be shown underneath the name of the package on the details screen. The field is in the same format as "Maintainer".', max_length=255, null=True, validators=[WEIPDCRM.models.version.validate_name], verbose_name='Author')),
                ('author_email', models.EmailField(blank=True, default='', max_length=255, null=True, verbose_name='Author Email')),
                ('sponsor_name', models.CharField(blank=True, default='', help_text='Finally, there might be someone who is simply providing the influence or the cash to make the package happen. This person should be listed here in the form of "Maintainer" except using a resource URI instead of an e-mail address.', max_length=255, null=True, validators=[WEIPDCRM.models.version.validate_name], verbose_name='Sponsor')),
                ('sponsor_site', models.URLField(blank=True, default='', max_length=255, null=True, verbose_name='Sponsor Site')),
                ('c_depiction', models.URLField(blank=True, default='', help_text='This is a URL that is loaded into an iframe, replacing the Description: and Homepage: .', null=True, verbose_name='Depiction')),
                ('custom_depiction', models.BooleanField(default=False, help_text='Exclude this version from Auto Depiction feature.', verbose_name='Custom Depiction')),
                ('c_homepage', models.URLField(blank=True, default='', help_text='Cydia supports a "More Info" field on the details screen that shunts users off to a website of the packager\'s choice.', null=True, verbose_name='Homepage')),
                ('c_priority', models.CharField(blank=True, choices=[(None, '-'), ('required', 'Required'), ('standard', 'Standard'), ('optional', 'Optional'), ('extra', 'Extra')], default='', help_text='Sets the importance of this package in relation to the system as a whole.  Common priorities are required, standard, optional, extra, etc.', max_length=255, null=True, verbose_name='Priority')),
                ('c_essential', models.CharField(blank=True, choices=[(None, '-'), ('yes', 'Yes'), ('no', 'No')], default='', help_text='This field is usually only needed when the answer is yes. It denotes a package that is required for proper operation of the system. Dpkg or any other installation tool will not allow an Essential package to be removed (at least not without using one of the force options).', max_length=255, null=True, verbose_name='Essential')),
                ('c_depends', models.TextField(blank=True, default='', help_text="List of packages that are required for this package to provide a non-trivial amount of functionality. The package maintenance software will not allow a package to be installed if the packages listed in its Depends field aren't installed (at least not without using the force options).  In an installation, the postinst scripts of packages listed in Depends fields are run before those of the packages which depend on them. On the opposite, in a removal, the prerm script of a package is run before those of the packages listed in its Depends field.", null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Depends')),
                ('c_pre_depends', models.TextField(blank=True, default='', help_text='List of packages that must be installed and configured before this one can be installed. This is usually used in the case where this package requires another package for running its preinst script.', null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Pre-Depends')),
                ('c_recommends', models.TextField(blank=True, default='', help_text='Lists packages that would be found together with this one in all but unusual installations. The package maintenance software will warn the user if they install a package without those listed in its Recommends field.', null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Recommends')),
                ('c_suggests', models.TextField(blank=True, default='', help_text='Lists packages that are related to this one and can perhaps enhance its usefulness, but without which installing this package is perfectly reasonable.', null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Suggests')),
                ('c_breaks', models.TextField(blank=True, default='', help_text='Lists packages that this one breaks, for example by exposing bugs when the named packages rely on this one. The package maintenance software will not allow broken packages to be configured; generally the resolution is to upgrade the packages named in a Breaks field.', null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Breaks')),
                ('c_conflicts', models.TextField(blank=True, default='', help_text='Lists packages that conflict with this one, for example by containing files with the same names. The package maintenance software will not allow conflicting packages to be installed at the same time. Two conflicting packages should each include a Conflicts line mentioning the other.', null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Conflicts')),
                ('c_replaces', models.TextField(blank=True, default='', help_text='List of packages files from which this one replaces. This is used for allowing this package to overwrite the files of another package and is usually used with the Conflicts field to force removal of the other package, if this one also has the same files as the conflicted package.', null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Replaces')),
                ('c_provides', models.TextField(blank=True, default='', help_text='This is a list of virtual packages that this one provides. Usually this is used in the case of several packages all providing the same service. For example, sendmail and exim can serve as a mail server, so they provide a common package ("mail-transport-agent") on which other packages can depend. This will allow sendmail or exim to serve as a valid option to satisfy the dependency.  This prevents the packages that depend on a mail server from having to know the package names for all of them, and using \'|\' to separate the list.', null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Provides')),
                ('c_origin', models.CharField(blank=True, default='', help_text='The name of the distribution this package is originating from.', max_length=255, null=True, verbose_name='Origin')),
                ('c_source', models.CharField(blank=True, default='', help_text='The name of the source package that this binary package came from, if it is different than the name of the package itself. If the source version differs from the binary version, then the source-name will be followed by a source-version in parenthesis.', max_length=255, null=True, verbose_name='Source')),
                ('c_build_essential', models.CharField(blank=True, choices=[(None, '-'), ('yes', 'Yes'), ('no', 'No')], default='', help_text='This field is usually only needed when the answer is yes, and is commonly injected by the archive software.  It denotes a package that is required when building other packages.', max_length=255, null=True, verbose_name='Build-Essential')),
                ('c_bugs', models.CharField(blank=True, default='', help_text='The url of the bug tracking system for this package. The current used format is bts-type://bts-address, like debbugs://bugs.debian.org.', max_length=255, null=True, validators=[WEIPDCRM.models.version.validate_bugs], verbose_name='Bugs')),
                ('c_multi_arch', models.CharField(blank=True, choices=[('no', 'No'), ('same', 'Same'), ('foreign', 'Foreign'), ('allowed', 'Allowed')], default='', help_text='This field is used to indicate how this package should behave on a multi-arch installations.<br /><ul><li>no - This value is the default when the field is omitted, in which case adding the field with an explicit no value is generally not needed.</li><li>same - This package is co-installable with itself, but it must not be used to satisfy the dependency of any package of a different architecture from itself.</li><li>foreign - This package is not co-installable with itself, but should be allowed to satisfy a non-arch-qualified dependency of a package of a different arch from itself (if a dependency has an explicit arch-qualifier then the value foreign is ignored).</li><li>allowed - This allows reverse-dependencies to indicate in their Depends field that they accept this package from a foreign architecture by qualifying the package name with :any, but has no effect otherwise.</li></ul>', max_length=255, null=True, verbose_name='Multi-Arch')),
                ('c_subarchitecture', models.CharField(blank=True, default='', max_length=255, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')], verbose_name='Subarchitecture')),
                ('c_kernel_version', models.CharField(blank=True, default='', max_length=255, null=True, validators=[WEIPDCRM.models.version.validate_version], verbose_name='Kernel-Version')),
                ('c_installer_menu_item', models.TextField(blank=True, default='', help_text='These fields are used by the debian-installer and are usually not needed. See /usr/share/doc/debian-installer/devel/modules.txt from the debian-installer package for more details about them.', null=True, verbose_name='Installer-Menu-Item')),
                ('c_built_using', models.TextField(blank=True, default='', help_text="This field lists extra source packages that were used during the build of this binary package.  This is an indication to the archive maintenance software that these extra source packages must be kept whilst this binary package is maintained. This field must be a list of source package names with strict '=' version relationships.  Note that the archive maintenance software is likely to refuse to accept an upload which declares a Built-Using relationship which cannot be satisfied within the archive.", null=True, validators=[WEIPDCRM.models.version.validate_relations], verbose_name='Built-Using')),
                ('c_built_for_profiles', models.TextField(blank=True, default='', help_text='This field specifies a whitespace separated list of build profiles that this binary packages was built with.', null=True, verbose_name='Built-For-Profiles')),
                ('c_section', models.ForeignKey(blank=True, default=None, help_text='Under the "Install" tab in Cydia, packages are listed by "Section". If you would like to encode a space into your section name, use an underscore (Cydia will automatically convert these).', null=True, on_delete=django.db.models.deletion.SET_NULL, to='WEIPDCRM.Section', verbose_name='Section')),
                ('device_compatibility', models.ManyToManyField(blank=True, to='WEIPDCRM.DeviceType', verbose_name='Device Compatibility')),
                ('os_compatibility', models.ManyToManyField(blank=True, to='WEIPDCRM.OSVersion', verbose_name='OS Compatibility')),
            ],
            options={
                'verbose_name': 'Version',
                'verbose_name_plural': 'Versions',
            },
        ),
        migrations.AddField(
            model_name='build',
            name='active_release',
            field=models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, to='WEIPDCRM.Release', verbose_name='Active Release'),
        ),
        migrations.RunSQL(
            "CREATE VIEW `package_view` AS SELECT `id`, `c_name`, `created_at`, `c_package`, `c_version`, `c_section_id`, `enabled`, `online_icon`, SUM(`download_times`) AS `download_count` FROM `WEIPDCRM_version` WHERE `enabled` = TRUE GROUP BY `c_package` ORDER BY `c_package`, `id` DESC;"
        ),
    ]
